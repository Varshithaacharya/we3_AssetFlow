from odoo import models, fields

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    asset_ids = fields.One2many(
        'asset.asset',
        'department_id',
        string='Allocated Assets'
    )
