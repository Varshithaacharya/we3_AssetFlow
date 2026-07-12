from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetAudit(models.Model):
    _name = 'asset.audit'
    _description = 'Asset Audit Cycle'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, id desc'

    name = fields.Char(string='Audit Name', required=True, copy=False, default='/', index=True)
    scope_type = fields.Selection([
        ('department', 'By Department'),
        ('location', 'By Location')
    ], string='Scope Type', default='department', required=True, tracking=True)
    department_id = fields.Many2one('hr.department', string='Department Scope', tracking=True)
    location = fields.Char(string='Location Scope', tracking=True)
    start_date = fields.Date(string='Start Date', required=True, default=fields.Date.context_today, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    auditor_ids = fields.Many2many(
        'hr.employee',
        'asset_audit_auditor_rel',
        'audit_id',
        'employee_id',
        string='Auditors',
        required=True
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Status', default='draft', required=True, tracking=True)
    line_ids = fields.One2many('asset.audit.line', 'audit_id', string='Audit Lines')

    @api.constrains('start_date', 'end_date')
    def _check_audit_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.end_date < rec.start_date:
                raise ValidationError(_("End date cannot be before start date."))

    @api.constrains('scope_type', 'department_id', 'location')
    def _check_scope(self):
        for rec in self:
            if rec.scope_type == 'department' and not rec.department_id:
                raise ValidationError(_("Department scope is required when Scope Type is 'By Department'."))
            if rec.scope_type == 'location' and not rec.location:
                raise ValidationError(_("Location scope is required when Scope Type is 'By Location'."))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('asset.audit.sequence') or '/'
        return super(AssetAudit, self).create(vals_list)

    def action_start_audit(self):
        for rec in self:
            if rec.state != 'draft':
                continue
            domain = []
            if rec.scope_type == 'department':
                domain = [('department_id', '=', rec.department_id.id)]
            elif rec.scope_type == 'location':
                domain = [('location', '=', rec.location)]
            
            assets = self.env['asset.asset'].search(domain)
            lines_val = []
            for asset in assets:
                lines_val.append((0, 0, {
                    'asset_id': asset.id,
                    'condition_before': asset.condition,
                    'status': 'verified',
                }))
            rec.write({
                'state': 'in_progress',
                'line_ids': lines_val
            })

    def action_complete_audit(self):
        for rec in self:
            if rec.state != 'in_progress':
                continue
            for line in rec.line_ids:
                if line.status == 'missing':
                    line.asset_id.write({'state': 'lost'})
                elif line.status == 'damaged':
                    line.asset_id.write({'condition': 'damaged'})
            rec.write({'state': 'completed'})


class AssetAuditLine(models.Model):
    _name = 'asset.audit.line'
    _description = 'Asset Audit Line'
    _order = 'id asc'

    audit_id = fields.Many2one('asset.audit', string='Audit Cycle', ondelete='cascade', required=True)
    asset_id = fields.Many2one('asset.asset', string='Asset', required=True)
    condition_before = fields.Selection([
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('damaged', 'Damaged')
    ], string='Condition Before Audit', required=True)
    status = fields.Selection([
        ('verified', 'Verified'),
        ('missing', 'Missing'),
        ('damaged', 'Damaged')
    ], string='Verification Status', default='verified', required=True)
    notes = fields.Text(string='Auditor Notes')

    @api.constrains('status', 'notes')
    def _check_notes_on_discrepancy(self):
        for rec in self:
            if rec.status in ('missing', 'damaged') and not rec.notes:
                raise ValidationError(_("Auditor notes must be provided when an asset is marked as missing or damaged."))
