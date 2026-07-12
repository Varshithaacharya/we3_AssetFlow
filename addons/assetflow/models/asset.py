from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetAsset(models.Model):
    _name = 'asset.asset'
    _description = 'Physical Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'asset_tag desc, name'

    name = fields.Char(string='Asset Name', required=True, tracking=True)
    category_id = fields.Many2one('asset.category', string='Category', required=True, tracking=True)
    asset_tag = fields.Char(string='Asset Tag', required=True, copy=False, default='/', index=True)
    serial_number = fields.Char(string='Serial Number', copy=False, index=True)
    acquisition_date = fields.Date(string='Acquisition Date', required=True, default=fields.Date.context_today)
    acquisition_cost = fields.Float(string='Acquisition Cost')
    condition = fields.Selection([
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('damaged', 'Damaged')
    ], string='Condition', default='new', required=True, tracking=True)
    location = fields.Char(string='Location', tracking=True)
    photo = fields.Binary(string='Photo')
    is_shared = fields.Boolean(string='Shared / Bookable', default=False)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('allocated', 'Allocated'),
        ('reserved', 'Reserved'),
        ('maintenance', 'Under Maintenance'),
        ('lost', 'Lost'),
        ('retired', 'Retired'),
        ('disposed', 'Disposed')
    ], string='Status', default='available', required=True, tracking=True, index=True)
    
    current_holder_id = fields.Many2one(
        'hr.employee', 
        string='Current Holder', 
        compute='_compute_current_holder', 
        store=False
    )
    
    allocation_ids = fields.One2many('asset.allocation', 'asset_id', string='Allocations')
    booking_ids = fields.One2many('asset.booking', 'asset_id', string='Bookings')
    maintenance_ids = fields.One2many('asset.maintenance', 'asset_id', string='Maintenance Requests')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_asset_tag', 'unique(asset_tag)', 'Asset Tag must be unique!'),
        ('unique_serial_number', 'unique(serial_number)', 'Serial Number must be unique!'),
    ]

    @api.depends('allocation_ids.state', 'allocation_ids.employee_id')
    def _compute_current_holder(self):
        for asset in self:
            active_alloc = asset.allocation_ids.filtered(lambda a: a.state in ('allocated', 'transfer_requested'))
            if active_alloc:
                asset.current_holder_id = active_alloc[0].employee_id
            else:
                asset.current_holder_id = False

    @api.constrains('acquisition_date')
    def _check_acquisition_date(self):
        for asset in self:
            if asset.acquisition_date and asset.acquisition_date > fields.Date.today():
                raise ValidationError(_("Acquisition date cannot be in the future."))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('asset_tag') or vals.get('asset_tag') == '/':
                vals['asset_tag'] = self.env['ir.sequence'].next_by_code('asset.asset.sequence') or '/'
        return super(AssetAsset, self).create(vals_list)
