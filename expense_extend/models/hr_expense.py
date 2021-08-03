from odoo import api, fields, models, _

class HrExpense(models.Model):

    _inherit = "hr.expense"

    @api.model
    def _default_department_id(self):
        return self.env.user.employee_id.department_id

    department_id = fields.Many2one('hr.department', string='Department', default=_default_department_id,
                                    states={'draft': [('readonly', False)], 'reported': [('readonly', False)],
                                            'refused': [('readonly', False)]},)
    branch_id = fields.Many2one("res.branch", string='Branch', default=lambda self: self.env.user.branch_id, index=True,
                                states={'draft': [('readonly', False)], 'reported': [('readonly', False)],
                                        'refused': [('readonly', False)]},)

    @api.onchange('employee_id')
    def onchange_employee_department(self):
        if self.employee_id:
            self.department_id = self.employee_id.department_id

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            branches = self.env.user.branch_ids.filtered(lambda m: m.company_id.id == self.company_id.id).ids
            self.branch_id = False
            if len(branches) > 0:
                self.branch_id = branches[0]
        else:
            return {'domain': {'branch_id': []}}


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    branch_id = fields.Many2one("res.branch", string='Branch', default=lambda self: self.env.user.branch_id, index=True,
                                states={'draft': [('readonly', False)], 'reported': [('readonly', False)],
                                        'refused': [('readonly', False)]}, )

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            branches = self.env.user.branch_ids.filtered(lambda m: m.company_id.id == self.company_id.id).ids
            self.branch_id = False
            if len(branches) > 0:
                self.branch_id = branches[0]
        else:
            return {'domain': {'branch_id': []}}