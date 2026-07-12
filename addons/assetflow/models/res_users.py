from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    reset_password_token = fields.Char(string='Reset Password Token')
