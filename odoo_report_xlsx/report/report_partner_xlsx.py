# Copyright 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.odoo_report_xlsx.partner_xlsx'
    _description = 'Odoo Report Xlsx'
    _inherit = 'report.odoo_report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            sheet = workbook.add_worksheet('Report')
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
