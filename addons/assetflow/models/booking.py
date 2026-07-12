from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetBooking(models.Model):
    _name = 'assetflow.booking'
    _description = 'Resource Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_start desc, id desc'

    resource_id = fields.Many2one(
        'assetflow.asset',
        string='Resource / Asset',
        required=True,
        domain=[('is_bookable', '=', True)],
        tracking=True
    )
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    date_start = fields.Datetime(string='Start Time', required=True, tracking=True)
    date_end = fields.Datetime(string='End Time', required=True, tracking=True)
    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='upcoming', required=True, tracking=True)
    
    has_conflict = fields.Boolean(string='Has Conflict', compute='_compute_has_conflict')
    reminder = fields.Boolean(string='Send Reminder Notification', default=False)

    @api.depends('date_start', 'date_end', 'resource_id', 'state')
    def _compute_has_conflict(self):
        for rec in self:
            if rec.state == 'cancelled' or not rec.resource_id or not rec.date_start or not rec.date_end:
                rec.has_conflict = False
                continue
            domain = [
                ('resource_id', '=', rec.resource_id.id),
                ('state', '!=', 'cancelled'),
                ('id', '!=', rec.id or 0),
                ('date_start', '<', rec.date_end),
                ('date_end', '>', rec.date_start)
            ]
            overlap = self.search_count(domain)
            rec.has_conflict = overlap > 0

    @api.constrains('date_start', 'date_end')
    def _check_timeslot(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_end <= rec.date_start:
                raise ValidationError(_("End time must be after start time."))

    @api.constrains('date_start', 'date_end', 'resource_id', 'state')
    def _check_overlap(self):
        for rec in self:
            if rec.state == 'cancelled':
                continue
            if rec.date_start and rec.date_end:
                domain = [
                    ('resource_id', '=', rec.resource_id.id),
                    ('state', '!=', 'cancelled'),
                    ('id', '!=', rec.id),
                    ('date_start', '<', rec.date_end),
                    ('date_end', '>', rec.date_start)
                ]
                overlapping_bookings = self.search(domain)
                if overlapping_bookings:
                    raise ValidationError(_(
                        "Booking conflict! The resource '%s' is already booked during this period (from %s to %s)."
                    ) % (rec.resource_id.name, overlapping_bookings[0].date_start, overlapping_bookings[0].date_end))

    def action_reschedule(self):
        pass

    def action_cancel(self):
        self.write({'state': 'cancelled'})
