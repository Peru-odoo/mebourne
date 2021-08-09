from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if vals.get('name', _('New')) == _('New'):
            if res.branch_id and not res.name:
                sequence_id = self.env['res.branch'].browse(vals['branch_id']).sequence_id
                if sequence_id:
                    res.name = S + '/' + sequence_id._next()
        return res
