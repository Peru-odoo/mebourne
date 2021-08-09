from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        if vals.get('name', 'New') == 'New':
            if res.branch_id and not res.name:
                po_sequence_id = self.env['res.branch'].browse(vals['branch_id']).po_sequence_id
                if po_sequence_id:
                    res.name = po_sequence_id._next()
        return res




