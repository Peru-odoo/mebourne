from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if vals.get('name', _('New')) == _('New'):
            if res.branch and not res.name:
                so_sequence_id = self.env['res.branch'].browse(vals['branch_id']).so_sequence_id
                if so_sequence_id:
                    res.name = so_sequence_id._next()
        return res