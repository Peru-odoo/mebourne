from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Branch(models.Model):
    _inherit = 'res.branch'

    code = fields.Char('Code', required=True, copy=False)
    sequence_id = fields.Many2one('ir.sequence', string='Entry Sequence', required=True, copy=False)
    sequence_number_next = fields.Integer(string='Next Number', compute='_compute_seq_number_next',
                                          inverse='_inverse_seq_number_next')

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The branch code must be unique !')
    ]

    @api.depends('sequence_id.number_next_actual')
    def _compute_seq_number_next(self):
        for branch in self:
            if branch.sequence_id:
                sequence = branch.sequence_id._get_current_sequence()
                branch.sequence_number_next = sequence.number_next_actual
            else:
                branch.sequence_number_next = 1

    def _inverse_seq_number_next(self):
        for branch in self:
            if branch.sequence_id and branch.sequence_number_next:
                sequence = branch.sequence_id._get_current_sequence()
                sequence.sudo().number_next = branch.sequence_number_next

    @api.model
    def _get_sequence_prefix(self, code):
        prefix = code.upper()
        return prefix + '/%(range_year)s/'

    @api.model
    def _create_sequence(self, vals):
        prefix = self._get_sequence_prefix(vals['code'])
        seq_name = vals['code']
        seq = {
            'name': _('%s Sequence') % seq_name,
            'implementation': 'no_gap',
            'prefix': prefix,
            'padding': 3,
            'number_increment': 1,
            'use_date_range': False,
        }
        seq = self.env['ir.sequence'].create(seq)
        return seq

    @api.model
    def create(self, vals):
        if not vals.get('sequence_id'):
            vals.update({'sequence_id': self.sudo()._create_sequence(vals).id})
        branch = super(Branch, self).create(vals)
        return branch



