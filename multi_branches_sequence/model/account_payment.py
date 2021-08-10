from odoo import models, fields, api, _
from odoo.exceptions import UserError


class account_payment(models.Model):
    _inherit = "account.payment"

    def post(self):
        res = super(account_payment, self).post()
        for rec in self:
            branch = rec.branch_id
            if rec.partner_type == 'customer':
                if rec.payment_type == 'inbound':
                    sequence_id = self.env['res.branch'].browse(branch).cus_sequence_id
                    if sequence_id:
                        rec.name = sequence_id._next()
                    else:
                        raise UserError(_("Please define a sequence on your branch."))

            if rec.partner_type == 'supplier':
                if rec.payment_type == 'inbound':
                    sequence_id = self.env['res.branch'].browse(branch).ven_sequence_id
                    if sequence_id:
                        rec.name = sequence_id._next()
                    else:
                        raise UserError(_("Please define a sequence on your branch."))
        return res