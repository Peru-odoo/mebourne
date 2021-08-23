from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    street = fields.Char(string='Street',related='partner_id.street')
    street2 = fields.Char(related='partner_id.street2',string='street2')
    township_id = fields.Many2one("res.township",related="partner_id.township_id",readonly=True)
    city = fields.Char(related='partner_id.city',string='City')
    zip = fields.Char(related='partner_id.zip',string='zip')
    ph_no = fields.Char(related='partner_id.phone')
    country_id = fields.Many2one("res.country",related="partner_id.country_id",readonly=True)