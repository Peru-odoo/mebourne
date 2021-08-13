from odoo import api, fields, models, _

class HrExpenseSheet(models.Model):

    _inherit = "hr.expense.sheet"

    first_signature = fields.Binary(string='First approval signature', attachment=True)
    second_signature = fields.Binary(string='Second approval signature', attachment=True)

    def first_approve_expense_sheets(self):
        res = super(HrExpenseSheet, self).first_approve_expense_sheets()
        self.first_signature = self.env.user.user_signature
        return res

    def approve_expense_sheets(self):
        res = super(HrExpenseSheet, self).approve_expense_sheets()
        self.second_signature = self.env.user.user_signature
        return res



