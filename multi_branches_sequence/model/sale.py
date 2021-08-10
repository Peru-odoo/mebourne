from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        branch = vals.get("branch_id", False)
        if branch:
            sequence_id = self.env['res.branch'].browse(branch).so_sequence_id
            vals["name"] = sequence_id._next() or "/"
        return super(SaleOrder, self).create(vals)

