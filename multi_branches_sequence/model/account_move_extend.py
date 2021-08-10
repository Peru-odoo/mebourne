from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_sequence(self):
            ''' Return the sequence to be used during the post of the current move.
            :return: An ir.sequence record or False.
            '''
            self.ensure_one()

            journal = self.journal_id
            branch = self.branch_id
            if self.type in ('entry', 'out_invoice') or not journal.refund_sequence:
                return branch.inv_sequence_id
            if self.type in ('entry', 'in_invoice') or not journal.refund_sequence:
                return branch.bill_sequence_id
            if not journal.refund_sequence_id:
                return
            return journal.refund_sequence_id
