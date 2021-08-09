from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_branch_sequence(self):
        if self.branch_id and not self.name:
            sequence_id = self.env['res.branch'].browse(vals['branch_id']).sequence_id
            if sequence_id:
                self.name = sequence_id._next()

    def _get_sequence(self):
        if self.branch_id:
            ''' Return the sequence to be used during the post of the current move.
            :return: An ir.sequence record or False.
            '''
            self.ensure_one()

            journal = self.journal_id
            if self.type in ('entry', 'out_invoice', 'in_invoice', 'out_receipt', 'in_receipt') or not journal.refund_sequence:
                if self.branch_id and not self.name:
                    sequence_id = self.env['res.branch'].browse(vals['branch_id']).sequence_id
                    if sequence_id:
                        # self.name = sequence_id._next()
                        return sequence_id._next()
            if not journal.refund_sequence_id:
                return
            return journal.refund_sequence_id
        else:
            ''' Return the sequence to be used during the post of the current move.
            :return: An ir.sequence record or False.
            '''
            self.ensure_one()

            journal = self.journal_id
            if self.type in ('entry', 'out_invoice', 'in_invoice', 'out_receipt', 'in_receipt') or not journal.refund_sequence:
                return journal.sequence_id
            if not journal.refund_sequence_id:
                return
            return journal.refund_sequence_id

