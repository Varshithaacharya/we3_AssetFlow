from odoo import models, fields, api

class AssetNotification(models.Model):
    _name = 'assetflow.notification'
    _description = 'AssetFlow Notification'
    _order = 'create_date desc, id desc'

    name = fields.Char(string='Title', required=True)
    employee_id = fields.Many2one('hr.employee', string='Recipient', required=True, index=True)
    message = fields.Text(string='Message', required=True)
    is_read = fields.Boolean(string='Is Read', default=False, required=True, index=True)
    res_model = fields.Char(string='Source Model')
    res_id = fields.Integer(string='Source ID')
    notification_type = fields.Selection([
        ('assignment', 'Assignment'),
        ('alert', 'Return Alert'),
        ('approval', 'Approval'),
        ('reminder', 'Reminder')
    ], string='Type', default='alert', required=True)

    def action_mark_as_read(self):
        self.write({'is_read': True})

    def action_mark_all_as_read(self):
        # Mark all notifications for the current employee (or all) as read
        self.search([('is_read', '=', False)]).write({'is_read': True})


class AssetActivity(models.Model):
    _name = 'assetflow.activity'
    _description = 'Operational Activity Log'
    _order = 'timestamp desc, id desc'

    actor_id = fields.Many2one('res.users', string='Actor', default=lambda self: self.env.user, required=True)
    action = fields.Char(string='Action', required=True)
    res_name = fields.Char(string='Related Record', required=True)
    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now, required=True)
