from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    total_paid_amount = fields.Char(string='Payment Amount', compute='_get_total_')

    @api.depends('amount_total', 'amount_residual')
    def _get_total_(self):
        for rec in self:
            total_amount= rec.amount_total - rec.amount_residual
            rec.total_paid_amount = format(total_amount, ".2f") + ' K'

