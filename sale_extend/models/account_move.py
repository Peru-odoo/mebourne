from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    sales_man_id = fields.Many2one(
        'hr.employee',
        string="Salesman",
        copy=False,
        track_visibility='onchange'
    )
    sale_by = fields.Many2one('hr.employee', string="Sales Person",compute='_get_sale_by')
    contact_id = fields.Char(string='Contact Name')
    contact_phone = fields.Char('Contact Phone')
    contact_address = fields.Char('Contact Address')
    accept_person = fields.Char(string='Accept Person')

    def _get_sale_by(self):
        for rec in self:

            if rec.invoice_origin is not None:

                rec.sale_by= self.env['sale.order'].search(
                    [('name', '=', rec.invoice_origin)]).sale_by

