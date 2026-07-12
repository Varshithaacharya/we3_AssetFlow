from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetAllocation(models.Model):
    _name = 'assetflow.allocation'
    _description = 'Asset Allocation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'allocation_date desc, id desc'

    asset_id = fields.Many2one('assetflow.asset', string='Asset', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    allocated_by_id = fields.Many2one('hr.employee', string='Allocated By', required=True)
    allocation_date = fields.Date(string='Allocation Date', required=True, default=fields.Date.context_today, tracking=True)
    expected_return_date = fields.Date(string='Expected Return Date', tracking=True)
    actual_return_date = fields.Date(string='Actual Return Date', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requested', 'Requested'),
        ('approved', 'Approved'),
        ('allocated', 'Allocated'),
        ('transfer', 'Transfer Requested'),
        ('returned', 'Returned')
    ], string='Status', default='draft', required=True, tracking=True)
    checkin_notes = fields.Text(string='Check-in Notes')
    is_overdue = fields.Boolean(string='Is Overdue', compute='_compute_is_overdue', search='_search_is_overdue')
    
    is_currently_allocated = fields.Boolean(compute='_compute_current_status')
    current_holder_id = fields.Many2one('hr.employee', compute='_compute_current_status')

    @api.depends('asset_id')
    def _compute_current_status(self):
        for rec in self:
            if rec.asset_id and rec.asset_id.state == 'allocated':
                rec.is_currently_allocated = True
                active_alloc = rec.asset_id.allocation_ids.filtered(lambda a: a.state == 'allocated')
                rec.current_holder_id = active_alloc[0].employee_id if active_alloc else False
            else:
                rec.is_currently_allocated = False
                rec.current_holder_id = False

    @api.depends('expected_return_date', 'actual_return_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for rec in self:
            if rec.state == 'allocated' and rec.expected_return_date and not rec.actual_return_date:
                rec.is_overdue = rec.expected_return_date < today
            else:
                rec.is_overdue = False

    def _search_is_overdue(self, operator, value):
        today = fields.Date.today()
        if operator == '=':
            if value:
                return [('state', '=', 'allocated'), ('expected_return_date', '<', today), ('actual_return_date', '=', False)]
            else:
                return ['|', '|', ('state', '!=', 'allocated'), ('expected_return_date', '>=', today), ('actual_return_date', '=', False)]
        return []

    @api.constrains('employee_id', 'department_id')
    def _check_allocation_target(self):
        for rec in self:
            if not rec.employee_id and not rec.department_id:
                raise ValidationError(_("An allocation must be assigned to either an Employee or a Department."))
            if rec.employee_id and rec.department_id:
                raise ValidationError(_("An allocation cannot be assigned to both an Employee and a Department simultaneously."))

    @api.constrains('allocation_date', 'expected_return_date')
    def _check_return_dates(self):
        for rec in self:
            if rec.expected_return_date and rec.expected_return_date < rec.allocation_date:
                raise ValidationError(_("Expected return date cannot be before the allocation date."))

    @api.constrains('asset_id', 'state')
    def _check_double_allocation(self):
        for rec in self:
            if rec.state in ('allocated', 'transfer'):
                domain = [
                    ('asset_id', '=', rec.asset_id.id),
                    ('state', 'in', ('allocated', 'transfer')),
                    ('id', '!=', rec.id)
                ]
                other_allocations = self.search_count(domain)
                if other_allocations > 0:
                    raise ValidationError(_("Asset '%s' is already allocated elsewhere or has a pending transfer request.") % rec.asset_id.name)

    @api.model_create_multi
    def create(self, vals_list):
        records = super(AssetAllocation, self).create(vals_list)
        for record in records:
            record._sync_asset_state()
        return records

    def write(self, vals):
        res = super(AssetAllocation, self).write(vals)
        if 'state' in vals:
            for record in self:
                record._sync_asset_state()
        return res

    def _sync_asset_state(self):
        for rec in self:
            if rec.state == 'allocated':
                rec.asset_id.write({
                    'state': 'allocated',
                    'department_id': rec.department_id.id or rec.employee_id.department_id.id
                })
            elif rec.state == 'returned':
                rec.asset_id.write({
                    'state': 'available'
                })
                if not rec.actual_return_date:
                    rec.actual_return_date = fields.Date.today()

    def action_allocate(self):
        self.write({'state': 'allocated'})

    def action_request_transfer(self):
        self.write({'state': 'requested'})

    def action_approve_transfer(self):
        self.write({'state': 'approved'})

    def action_complete_reallocation(self):
        self.ensure_one()
        # Find and release old allocations
        active_allocs = self.env['assetflow.allocation'].search([
            ('asset_id', '=', self.asset_id.id),
            ('state', '=', 'allocated')
        ])
        active_allocs.write({'state': 'returned', 'actual_return_date': fields.Date.today()})
        self.write({'state': 'allocated'})

    def action_mark_returned(self):
        self.write({'state': 'returned', 'actual_return_date': fields.Date.today()})
