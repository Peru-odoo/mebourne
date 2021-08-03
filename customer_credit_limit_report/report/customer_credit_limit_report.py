from odoo import tools
from odoo import api, fields, models, _

class CustomerCreditLimitReport(models.Model):
    _name = "credit.limit.report"
    _description = "Customer Credit Limit Report"
    _auto = False
    _order = 'id desc'
    
    partner_id = fields.Many2one("res.partner",string="Customer Name")
    credit_limit_amount = fields.Float("Credit Limit Amount")
    payment_term_id  = fields.Many2one("account.payment.term",string="Payment Term")
    invoice_date = fields.Date("Invoice Date")
    due_date = fields.Date("Due Date")
    invoice_number = fields.Char("Invoice No")
    invoice_amount = fields.Float("Invoice Amount")

    def _query(self, with_clause='', fields={}, groupby='', from_clause='', where=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
            am.id as id,
            am.partner_id as partner_id,
            partner.credit_limit as credit_limit_amount,
            am.invoice_payment_term_id as payment_term_id,
            am.invoice_date as invoice_date,
            am.invoice_date_due as due_date,
            am.name as invoice_number,
            am.amount_total as invoice_amount
        """
        for field in fields.values():
            select_ += field
        from_ = """
                account_move am
                    left join res_partner partner on am.partner_id = partner.id
                %s
        """ % from_clause

        where_ = """
            am.state !='cancel' and
            am.type = 'out_invoice'
            %s
        """ % where

        groupby_ = """
            am.id,
            am.partner_id,
            partner.credit_limit,
            am.invoice_payment_term_id,
            am.invoice_date,
            am.invoice_date_due,
            am.name,
            am.amount_total            
            %s
        """ % (groupby)

        return '%s (SELECT %s FROM %s WHERE %s GROUP BY %s)' % (with_, select_, from_, where_, groupby_)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))