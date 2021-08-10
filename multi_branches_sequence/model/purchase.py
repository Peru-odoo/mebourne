from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        branch = vals.get("branch_id", False)
        if branch:
            sequence_id = self.env['res.branch'].browse(branch).po_sequence_id
            vals["name"] = sequence_id._next() or "/"
        return super(PurchaseOrder, self).create(vals)



