from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_sequence(self):
            self.ensure_one()
            journal = self.journal_id
            branch = self.branch_id
            if self.type in ('entry', 'out_invoice') or not journal.refund_sequence:
                return branch.inv_sequence_id
            if self.type in ('entry', 'in_invoice') or not journal.refund_sequence:
                return branch.bill_sequence_id
            if self.type in ('entry', 'out_refund') or not journal.refund_sequence:
                return branch.credit_sequence_id
            if self.type in ('entry', 'in_refund') or not journal.refund_sequence:
                return branch.refund_sequence_id
            if not journal.refund_sequence_id:
                return
            return journal.refund_sequence_id
