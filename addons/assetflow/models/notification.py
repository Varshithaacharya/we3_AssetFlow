from odoo import models, fields, api

class AssetNotification(models.Model):
    _name = 'asset.notification'
    _description = 'AssetFlow Notification'
    _order = 'create_date desc, id desc'

    name = fields.Char(string='Title', required=True)
    employee_id = fields.Many2one('hr.employee', string='Recipient', required=True, index=True)
    message = fields.Text(string='Message', required=True)
    is_read = fields.Boolean(string='Is Read', default=False, required=True, index=True)
    res_model = fields.Char(string='Source Model')
    res_id = fields.Integer(string='Source ID')
