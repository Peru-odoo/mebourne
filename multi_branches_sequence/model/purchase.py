from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        if vals.get('name', 'New') == 'New':
            branch = self.branch_id
            vals['name'] = branch.po_sequence_id
        return res




