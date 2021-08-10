from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if vals.get('name', _('New')) == _('New'):
            if res.branch_id:
                sequence_id = self.env['res.branch'].browse(vals['branch_id']).so_sequence_id
                if sequence_id:
                    vals['name'] = sequence_id._next()
                if 'company_id' in vals:
                    vals['name'] = sequence_id.with_context(force_company=vals['company_id'])._next()
        return res
