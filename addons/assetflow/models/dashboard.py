from odoo import models, fields, api
import json

class AssetDashboard(models.Model):
    _name = 'assetflow.dashboard'
    _description = 'AssetFlow Dashboard'

    name = fields.Char(string='Name', default='AssetFlow Operational Dashboard', required=True)
    
    kpi_assets_available = fields.Integer(string='Assets Available', compute='_compute_kpi_values')
    kpi_assets_allocated = fields.Integer(string='Assets Allocated', compute='_compute_kpi_values')
    kpi_maintenance_today = fields.Integer(string='Maintenance Today', compute='_compute_kpi_values')
    kpi_active_bookings = fields.Integer(string='Active Bookings', compute='_compute_kpi_values')
    kpi_pending_transfers = fields.Integer(string='Pending Transfers', compute='_compute_kpi_values')
    kpi_upcoming_returns = fields.Integer(string='Upcoming Returns', compute='_compute_kpi_values')
    overdue_returns_count = fields.Integer(string='Overdue Returns Count', compute='_compute_kpi_values')
    overdue_returns_json = fields.Char(string='Overdue Returns JSON', compute='_compute_kpi_values')

    def _compute_kpi_values(self):
        today = fields.Date.today()
        for rec in self:
            rec.kpi_assets_available = self.env['assetflow.asset'].search_count([('state', '=', 'available')])
            rec.kpi_assets_allocated = self.env['assetflow.asset'].search_count([('state', '=', 'allocated')])
            rec.kpi_maintenance_today = self.env['assetflow.maintenance'].search_count([('maintenance_date', '=', today)])
            # Active bookings: ongoing or upcoming
            rec.kpi_active_bookings = self.env['assetflow.booking'].search_count([('state', 'in', ('ongoing', 'upcoming'))])
            # Pending transfers: requested
            rec.kpi_pending_transfers = self.env['assetflow.allocation'].search_count([('state', '=', 'requested')])
            
            # Upcoming returns
            rec.kpi_upcoming_returns = self.env['assetflow.allocation'].search_count([
                ('state', '=', 'allocated'),
                ('expected_return_date', '>=', today)
            ])
            
            # Overdue returns
            overdue_allocs = self.env['assetflow.allocation'].search([
                ('state', '=', 'allocated'),
                ('expected_return_date', '<', today)
            ])
            rec.overdue_returns_count = len(overdue_allocs)
            
            overdue_list = []
            for alloc in overdue_allocs:
                overdue_list.append({
                    'asset_name': alloc.asset_id.name,
                    'employee_name': alloc.employee_id.name if alloc.employee_id else '',
                    'expected_return_date': alloc.expected_return_date.strftime('%Y-%m-%d') if alloc.expected_return_date else '',
                })
            rec.overdue_returns_json = json.dumps(overdue_list)
