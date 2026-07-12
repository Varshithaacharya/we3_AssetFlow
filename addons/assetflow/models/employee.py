from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    role = fields.Selection([
        ('employee', 'Employee'),
        ('dept_head', 'Department Head'),
        ('asset_manager', 'Asset Manager'),
        ('admin', 'Administrator')
    ], string='AssetFlow Role', default='employee', required=True, tracking=True)

    allocation_ids = fields.One2many(
        'assetflow.allocation',
        'employee_id',
        string='Asset Allocations'
    )
    booking_ids = fields.One2many(
        'assetflow.booking',
        'employee_id',
        string='Resource Bookings'
    )
    maintenance_ids = fields.One2many(
        'assetflow.maintenance',
        'reporter_id',
        string='Maintenance Requests'
    )
    audit_assignment_ids = fields.Many2many(
        'assetflow.audit.cycle',
        'assetflow_audit_auditor_rel',
        'employee_id',
        'audit_id',
        string='Assigned Audits'
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super(HrEmployee, self).create(vals_list)
        for record in records:
            if record.user_id:
                record._sync_user_groups()
        return records

    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        if 'role' in vals or 'user_id' in vals:
            for record in self:
                if record.user_id:
                    record._sync_user_groups()
        return res

    def _sync_user_groups(self):
        self.ensure_one()
        if not self.user_id:
            return
        
        # Resolve standard security groups defined in security/groups.xml and base Odoo groups
        group_emp = self.env.ref('assetflow.group_assetflow_employee', raise_if_not_found=False)
        group_dh = self.env.ref('assetflow.group_assetflow_dept_head', raise_if_not_found=False)
        group_am = self.env.ref('assetflow.group_asset_manager', raise_if_not_found=False)
        group_admin = self.env.ref('assetflow.group_assetflow_admin', raise_if_not_found=False)
        
        group_system = self.env.ref('base.group_system', raise_if_not_found=False)
        group_erp = self.env.ref('base.group_erp_manager', raise_if_not_found=False)
        group_hr_manager = self.env.ref('hr.group_hr_manager', raise_if_not_found=False)

        if not (group_emp and group_dh and group_am and group_admin):
            return  # Safety guard during module loading or tests

        # Prepare group updates
        groups_to_add = [group_emp]
        groups_to_remove = []

        if self.role == 'employee':
            groups_to_remove.extend([group_dh, group_am, group_admin])
            if group_system: groups_to_remove.append(group_system)
            if group_erp: groups_to_remove.append(group_erp)
            if group_hr_manager: groups_to_remove.append(group_hr_manager)
        elif self.role == 'dept_head':
            groups_to_add.append(group_dh)
            groups_to_remove.extend([group_am, group_admin])
            if group_system: groups_to_remove.append(group_system)
            if group_erp: groups_to_remove.append(group_erp)
            if group_hr_manager: groups_to_remove.append(group_hr_manager)
        elif self.role == 'asset_manager':
            groups_to_add.append(group_am)
            groups_to_remove.extend([group_dh, group_admin])
            if group_system: groups_to_remove.append(group_system)
            if group_erp: groups_to_remove.append(group_erp)
            if group_hr_manager: groups_to_remove.append(group_hr_manager)
        elif self.role == 'admin':
            groups_to_add.extend([group_dh, group_am, group_admin])
            if group_system: groups_to_add.append(group_system)
            if group_erp: groups_to_add.append(group_erp)
            if group_hr_manager: groups_to_add.append(group_hr_manager)

        vals = []
        for g in groups_to_add:
            vals.append((4, g.id))
        for g in groups_to_remove:
            vals.append((3, g.id))

        if vals:
            self.user_id.sudo().write({'groups_id': vals})
