from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    role = fields.Selection([
        ('employee', 'Employee'),
        ('dept_head', 'Department Head'),
        ('asset_manager', 'Asset Manager')
    ], string='AssetFlow Role', default='employee', required=True, tracking=True)

    allocation_ids = fields.One2many(
        'asset.allocation',
        'employee_id',
        string='Asset Allocations'
    )
    booking_ids = fields.One2many(
        'asset.booking',
        'employee_id',
        string='Resource Bookings'
    )
    maintenance_ids = fields.One2many(
        'asset.maintenance',
        'reporter_id',
        string='Maintenance Requests'
    )
    audit_assignment_ids = fields.Many2many(
        'asset.audit',
        'asset_audit_auditor_rel',
        'employee_id',
        'audit_id',
        string='Assigned Audits'
    )
