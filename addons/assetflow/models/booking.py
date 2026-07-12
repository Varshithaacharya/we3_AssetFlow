from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AssetBooking(models.Model):
    _name = 'asset.booking'
    _description = 'Resource Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_time desc, id desc'

    asset_id = fields.Many2one(
        'asset.asset',
        string='Resource / Asset',
        required=True,
        domain=[('is_shared', '=', True)],
        tracking=True
    )
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    start_time = fields.Datetime(string='Start Time', required=True, tracking=True)
    end_time = fields.Datetime(string='End Time', required=True, tracking=True)
    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='upcoming', required=True, tracking=True)

    @api.constrains('start_time', 'end_time')
    def _check_timeslot(self):
        for rec in self:
            if rec.start_time and rec.end_time and rec.end_time <= rec.start_time:
                raise ValidationError(_("End time must be after start time."))

    @api.constrains('start_time', 'end_time', 'asset_id', 'state')
    def _check_overlap(self):
        for rec in self:
            if rec.state == 'cancelled':
                continue
            if rec.start_time and rec.end_time:
                domain = [
                    ('asset_id', '=', rec.asset_id.id),
                    ('state', '!=', 'cancelled'),
                    ('id', '!=', rec.id),
                    ('start_time', '<', rec.end_time),
                    ('end_time', '>', rec.start_time)
                ]
                overlapping_bookings = self.search(domain)
                if overlapping_bookings:
                    raise ValidationError(_(
                        "Booking conflict! The resource '%s' is already booked during this period (from %s to %s)."
                    ) % (rec.asset_id.name, overlapping_bookings[0].start_time, overlapping_bookings[0].end_time))
