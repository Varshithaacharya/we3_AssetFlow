from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetCategory(models.Model):
    _name = 'assetflow.category'
    _description = 'Asset Category'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    parent_id = fields.Many2one('assetflow.category', string='Parent Category', ondelete='restrict')
    active = fields.Boolean(string='Active', default=True)
    warranty_required = fields.Boolean(string='Warranty Required', default=False)
    warranty_period = fields.Integer(string='Warranty Period (Months)', default=0)
    asset_ids = fields.One2many('assetflow.asset', 'category_id', string='Assets')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Category name must be unique!'),
    ]

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('Error! You cannot create recursive categories.'))

    @api.constrains('warranty_required', 'warranty_period')
    def _check_warranty_period(self):
        for category in self:
            if category.warranty_required and category.warranty_period <= 0:
                raise ValidationError(_('Warranty period must be a positive integer if warranty is required.'))
