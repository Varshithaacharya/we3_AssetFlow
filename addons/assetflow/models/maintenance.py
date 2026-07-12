from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetMaintenance(models.Model):
    _name = 'asset.maintenance'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, id desc'

    asset_id = fields.Many2one('asset.asset', string='Asset', required=True, tracking=True)
    description = fields.Text(string='Issue Description', required=True, tracking=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium', required=True, tracking=True)
    photo = fields.Binary(string='Photo')
    reporter_id = fields.Many2one('hr.employee', string='Reporter', required=True, default=lambda self: self.env.user.employee_id)
    technician_id = fields.Many2one('hr.employee', string='Assigned Technician', tracking=True)
    state = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ], string='Status', default='pending', required=True, tracking=True)
    resolution_notes = fields.Text(string='Resolution Notes', tracking=True)

    @api.constrains('state', 'resolution_notes')
    def _check_resolution_notes(self):
        for rec in self:
            if rec.state == 'resolved' and not rec.resolution_notes:
                raise ValidationError(_("Resolution notes must be provided when resolving a maintenance request."))

    @api.model_create_multi
    def create(self, vals_list):
        records = super(AssetMaintenance, self).create(vals_list)
        for record in records:
            record._sync_asset_state()
        return records

    def write(self, vals):
        res = super(AssetMaintenance, self).write(vals)
        if 'state' in vals:
            for record in self:
                record._sync_asset_state()
        return res

    def _sync_asset_state(self):
        for rec in self:
            if rec.state in ('approved', 'in_progress'):
                rec.asset_id.write({'state': 'maintenance'})
            elif rec.state in ('resolved', 'rejected'):
                rec.asset_id.write({'state': 'available'})
