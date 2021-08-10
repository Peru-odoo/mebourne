from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        if self.branch_id:
            sequence_id = self.env['res.branch'].browse(vals['branch_id']).so_sequence_id
            vals["name"] = sequence_id._next() or "/"
        return super(SaleOrder, self).create(vals)
