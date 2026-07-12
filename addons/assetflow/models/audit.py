from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetAudit(models.Model):
    _name = 'assetflow.audit.cycle'
    _description = 'Asset Audit Cycle'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_start desc, id desc'

    name = fields.Char(string='Audit Name', required=True, copy=False, default='/', index=True)
    scope = fields.Char(string='Scope', required=True, tracking=True)
    date_start = fields.Date(string='Start Date', required=True, default=fields.Date.context_today, tracking=True)
    date_end = fields.Date(string='End Date', required=True, tracking=True)
    auditor_ids = fields.Many2many(
        'hr.employee',
        'assetflow_audit_auditor_rel',
        'audit_id',
        'employee_id',
        string='Auditors',
        required=True
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ], string='Status', default='draft', required=True, tracking=True)
    line_ids = fields.One2many('assetflow.audit.line', 'audit_id', string='Audit Lines')
    discrepancy_count = fields.Integer(string='Discrepancies', compute='_compute_discrepancies')

    @api.depends('line_ids.result')
    def _compute_discrepancies(self):
        for rec in self:
            rec.discrepancy_count = len(rec.line_ids.filtered(lambda l: l.result in ('missing', 'damaged')))

    @api.constrains('date_start', 'date_end')
    def _check_audit_dates(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_end < rec.date_start:
                raise ValidationError(_("End date cannot be before start date."))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('assetflow.audit.sequence') or '/'
        return super(AssetAudit, self).create(vals_list)

    def action_start_audit(self):
        for rec in self:
            if rec.state != 'draft':
                continue
            # Search for assets in departments or locations containing the scope text
            domain = []
            if rec.scope:
                domain = ['|', ('department_id.name', 'ilike', rec.scope), ('location', 'ilike', rec.scope)]
            assets = self.env['assetflow.asset'].search(domain)
            if not assets:
                assets = self.env['assetflow.asset'].search([]) # fallback
                
            lines_val = []
            for asset in assets:
                lines_val.append((0, 0, {
                    'asset_id': asset.id,
                    'result': 'verified',
                    'auditor_id': rec.auditor_ids[0].id if rec.auditor_ids else False,
                }))
            rec.write({
                'state': 'in_progress',
                'line_ids': lines_val
            })

    def action_close_audit_cycle(self):
        for rec in self:
            if rec.state != 'in_progress':
                continue
            for line in rec.line_ids:
                if line.result == 'missing':
                    line.asset_id.write({'state': 'lost'})
                elif line.result == 'damaged':
                    line.asset_id.write({'condition': 'damaged'})
            rec.write({'state': 'closed'})

    def action_view_discrepancies(self):
        self.ensure_one()
        return {
            'name': _('Discrepancies'),
            'type': 'ir.actions.act_window',
            'res_model': 'assetflow.audit.line',
            'view_mode': 'tree',
            'domain': [('audit_id', '=', self.id), ('result', 'in', ('missing', 'damaged'))],
            'target': 'current',
        }


class AssetAuditLine(models.Model):
    _name = 'assetflow.audit.line'
    _description = 'Asset Audit Line'
    _order = 'id asc'

    audit_id = fields.Many2one('assetflow.audit.cycle', string='Audit Cycle', ondelete='cascade', required=True)
    asset_id = fields.Many2one('assetflow.asset', string='Asset', required=True)
    result = fields.Selection([
        ('verified', 'Verified'),
        ('missing', 'Missing'),
        ('damaged', 'Damaged')
    ], string='Verification Result', default='verified', required=True)
    notes = fields.Text(string='Auditor Notes')
    auditor_id = fields.Many2one('hr.employee', string='Auditor', required=True)

    @api.constrains('result', 'notes')
    def _check_notes_on_discrepancy(self):
        for rec in self:
            if rec.result in ('missing', 'damaged') and not rec.notes:
                raise ValidationError(_("Auditor notes must be provided when an asset is marked as missing or damaged."))
