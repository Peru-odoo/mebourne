from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if vals.get('name', _('New')) == _('New'):
            if vals.get('name', 'New') == 'New':
                branch = self.branch_id
                vals['name'] = branch.so_sequence_id
        return res