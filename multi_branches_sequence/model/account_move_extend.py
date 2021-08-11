from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_sequence(self):
        res = super(AccountMove, self)._get_sequence()
        journal = self.journal_id
        branch = self.branch_id
        if self.type in ('entry', 'out_invoice', 'out_receipt') or not journal.refund_sequence:
            return branch.inv_sequence_id
        if self.type in ('entry', 'in_invoice', 'in_receipt') or not journal.refund_sequence:
            return branch.bill_sequence_id
        return res
