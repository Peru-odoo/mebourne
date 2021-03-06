from odoo import models, fields, api, _
from odoo.tools.misc import xlwt
import io
import base64
from xlwt import easyxf
from PIL import Image
from dateutil.relativedelta import relativedelta
from datetime import datetime
import time


class SaleReportRegion(models.TransientModel):
    _name = "sale.report.region"
    _description = "Sale Report By Region"

    start_date = fields.Date('From Date', required=True, default=time.strftime('%Y-01-01'))
    end_date = fields.Date('To Date', required=True, default=time.strftime('%Y-12-01'))
    sale_report_region_file = fields.Binary('Sale Report By Region')
    file_name = fields.Char('File Name')
    sale_report_region_printed = fields.Boolean('Sale Report by Region Printed')

    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.user.company_id
    )

    def action_print_sale_region(self):
        custom_value = {}
        workbook = xlwt.Workbook()
        column_heading_style = easyxf(
            'font:height 200;font:bold True;align:vertical center, horiz center;' "borders: top thin,bottom thin,right thin,left thin")

        data_style = easyxf(
            'font:height 200;align:vertical center,horiz center;'"borders: top thin,bottom thin,right thin,left thin")

        worksheet = workbook.add_sheet('Sale Report by region')
        worksheet.write_merge(4, 5, 0, 0, _('Region'), column_heading_style)
        

        worksheet.write_merge(4, 4, 1, 2, _('Jan'), column_heading_style)
        worksheet.write(5, 1, _('Qty'), column_heading_style)
        worksheet.write(5, 2, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 3, 4, _('Feb'), column_heading_style)
        worksheet.write(5, 3, _('Qty'), column_heading_style)
        worksheet.write(5, 4, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 5, 6, _('Mar'), column_heading_style)
        worksheet.write(5, 5, _('Qty'), column_heading_style)
        worksheet.write(5, 6, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 7, 8, _('Apr'), column_heading_style)
        worksheet.write(5, 7, _('Qty'), column_heading_style)
        worksheet.write(5, 8, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 9, 10, _('May'), column_heading_style)
        worksheet.write(5, 9, _('Qty'), column_heading_style)
        worksheet.write(5, 10, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 11, 12, _('Jun'), column_heading_style)
        worksheet.write(5, 11, _('Qty'), column_heading_style)
        worksheet.write(5, 12, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 13, 14, _('Jul'), column_heading_style)
        worksheet.write(5, 13, _('Qty'), column_heading_style)
        worksheet.write(5, 14, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 15, 16, _('Aug'), column_heading_style)
        worksheet.write(5, 15, _('Qty'), column_heading_style)
        worksheet.write(5, 16, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 17, 18, _('Sep'), column_heading_style)
        worksheet.write(5, 17, _('Qty'), column_heading_style)
        worksheet.write(5, 18, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 19, 20, _('Oct'), column_heading_style)
        worksheet.write(5, 19, _('Qty'), column_heading_style)
        worksheet.write(5, 20, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 21, 22, _('Nov'), column_heading_style)
        worksheet.write(5, 21, _('Qty'), column_heading_style)
        worksheet.write(5, 22, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 23, 24, _('Dec'), column_heading_style)
        worksheet.write(5, 23, _('Qty'), column_heading_style)
        worksheet.write(5, 24, _('Amount'), column_heading_style)
        worksheet.write_merge(4, 4, 25, 26, _('Total'), column_heading_style)
        worksheet.write(5, 25, _('Qty'), column_heading_style)
        worksheet.write(5, 26, _('Amount'), column_heading_style)

        jan = feb = mar = apr = may = jun = jul = aug = sep = octo = nov = dec = 0
        jan_qty = feb_qty = mar_qty = apr_qty = may_qty = jun_qty = jul_qty = aug_qty = sep_qty = oct_qty = nov_qty = dec_qty = 0

        tmp1 = tmp2 = tmp3 = tmp4 = tmp5 = tmp6 = tmp7 = tmp8 = tmp9 = tmp10 = tmp11 = tmp12 = 0
        tmp_qty1 = tmp_qty2 = tmp_qty3 = tmp_qty4 = tmp_qty5 = tmp_qty6 = tmp_qty7 = tmp_qty8 = tmp_qty9 = tmp_qty10 = tmp_qty11 = tmp_qty12 = 0

        worksheet.row(4).height_mismatch = True
        worksheet.row(4).height = 350
        worksheet.col(0).width = 5000

        col_count = 1
        while col_count < 26:
            worksheet.col(col_count).width = 3000
            col_count += 1

        state_obj = self.env['res.country.state'].sudo()

        added_date = month = year = None
        start_date = self.start_date
        end_date = self.end_date

        end_month = end_date.month
        start_month = start_date.month

        row = 6
        month_count = 12
        col = 0
        row_total_qty = 0
        row_total_amount = 0
        amount = 0
        qty = 0
        for wizard in self:
            heading = 'Sale Report by Region'
            heading1 = self.company_id.name
            heading2 = 'Document No : '
            heading3 = 'Page: 1/1'
            # worksheet.insert_image(1, 1, 0, 3, img)
            worksheet.write_merge(1, 1, 4, 8, heading1, easyxf('font:height 200;font:bold True;align: horiz center;'))
            worksheet.write_merge(1, 1, 11, 15, heading2, easyxf('font:height 200;font:bold True;align: horiz center;'))
            worksheet.write_merge(1, 1, 20, 22, heading3, easyxf('font:height 200;font:bold True;align: horiz center;'))
            worksheet.write_merge(3, 3, 0, 26, heading, easyxf(
                'font:height 200; align: horiz center;font:bold True;' "borders: top thin,bottom thin"))

            region_stat = """SELECT distinct r.state_id FROM res_partner r,sale_order s 
                            WHERE s.invoice_status='invoiced'
                            and r.id=s.partner_id""";
            self.env.cr.execute(region_stat)
            record = self.env.cr.dictfetchall()
            for rec in record:
                state = state_obj.browse(rec['state_id'])
                worksheet.write(row, 0, state.name, data_style)
                partner_stat = """SELECT id FROM res_partner WHERE state_id='""" + str(state.id) + """';"""
                self.env.cr.execute(partner_stat)
                partner_result = self.env.cr.dictfetchall()
                for par in partner_result:
                    month_count = 12
                    month = (start_date - relativedelta(months=month_count)).month
                    year = (start_date).year
                    next_month_start_date = start_date
                    # while (month <= end_month):
                    while (next_month_start_date <= end_date):
                        month = (start_date - relativedelta(months=month_count)).month
                        query = """SELECT sum(total) total,sum(qty) qty
                                    FROM(
                                    SELECT a.id as order_id,a.amount_total as total,sum(c.product_uom_qty) as qty
                                    FROM sale_order a,sale_order_line c
                                    WHERE a.partner_id = '""" + str(par['id']) + """' 
                                    AND a.invoice_status='invoiced'
                                    AND a.id  = c.order_id
                                    AND c.qty_invoiced != 0
                                    AND date_part('month', a.date_order) ='""" + str(month) + """'
                                    AND date_part('year', a.date_order) ='""" + str(year)+"""'
                                    group by a.id,a.amount_total
                                    ) as tmp;"""
                        self.env.cr.execute(query)
                        result = self.env.cr.dictfetchall()
                        for res in result:
                            amt = res['total']
                            # print("AMT",amt)
                            if res['total']:
                                # print("AMT",amt)
                                amount += amt
                                row_total_amount += amount
                                if month == 1:
                                    jan += amount
                                    tmp1 += amount
                                elif month == 2:
                                    feb += amount
                                    tmp2 += amount
                                elif month == 3:
                                    mar += amount
                                    tmp3 += amount
                                elif month == 4:
                                    apr += amount
                                    tmp4 += 4
                                elif month == 5:
                                    may += amount
                                    tmp5 += amount
                                elif month == 6:
                                    jun += amount
                                    tmp6 += amount
                                elif month == 7:
                                    jul += amount
                                    tmp7 += amount
                                    
                                elif month == 8:
                                    aug += amount
                                    tmp8 += amount
                                elif month == 9:
                                    sep += amount
                                    tmp9 += amount
                                elif month == 10:
                                    octo += amount
                                    tmp10 += amount
                                elif month == 11:
                                    nov += amount
                                    tmp11 += amount
                                else:
                                    dec += amount
                                    tmp12 += amount
                            quantity = res['qty']
                            if res['qty']:
                                qty += quantity
                                # print("QUAntity",quantity)
                                row_total_qty += qty
                                if month == 1:
                                    jan_qty += qty
                                    tmp_qty1 += qty
                                elif month == 2:
                                    feb_qty += qty
                                    tmp_qty2 += qty
                                elif month == 3:
                                    mar_qty += qty
                                    tmp_qty3 += qty
                                elif month == 4:
                                    apr_qty += qty
                                    tmp_qty4 += qty
                                elif month == 5:
                                    may_qty += qty
                                    tmp_qty5 += qty
                                elif month == 6:
                                    jun_qty += qty
                                    tmp_qty6 += qty
                                elif month == 7:
                                    jul_qty += qty
                                    tmp_qty7 += qty
                                elif month == 8:
                                    aug_qty += qty
                                    tmp_qty8 += qty
                                elif month == 9:
                                    sep_qty += qty
                                    tmp_qty9 += qty
                                elif month == 10:
                                    oct_qty += qty
                                    tmp_qty10 += qty
                                elif month == 11:
                                    nov_qty += qty
                                    tmp_qty11 += qty
                                else:
                                    dec_qty += qty
                                    tmp_qty12 += qty
                            amount = 0
                            qty = 0
                        month_count -= 1
                        month = (start_date - relativedelta(months=month_count)).month
                        next_month_start_date = next_month_start_date + relativedelta(months=1)
                        year = next_month_start_date.year
                        # if month_count == 0:
                        #     break

                # data print on excel
                month_count = 12
                month = (start_date - relativedelta(months=month_count)).month
                while (month <= end_month):
                    col = (month * 2)
                    if month == 1:
                        worksheet.write(row, col, tmp1 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty1 or '-', data_style)
                    elif month == 2:
                        worksheet.write(row, col, tmp2 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty2 or '-', data_style)
                    elif month == 3:
                        worksheet.write(row, col, tmp3 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty3 or '-', data_style)
                    elif month == 4:
                        worksheet.write(row, col, tmp4 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty4 or '-', data_style)
                    elif month == 5:
                        worksheet.write(row, col, tmp5 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty5 or '-', data_style)
                    elif month == 6:
                        worksheet.write(row, col, tmp6 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty6 or '-', data_style)
                    elif month == 7:
                        worksheet.write(row, col, tmp7 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty7 or '-', data_style)
                    elif month == 8:
                        worksheet.write(row, col, tmp8 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty8 or '-', data_style)
                    elif month == 9:
                        worksheet.write(row, col, tmp9 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty9 or '-', data_style)
                    elif month == 10:
                        worksheet.write(row, col, tmp10 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty10 or '-', data_style)
                    elif month == 11:
                        worksheet.write(row, col, tmp11 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty11 or '-', data_style)
                    else:
                        worksheet.write(row, col, tmp12 or '-', data_style)
                        worksheet.write(row, col - 1, tmp_qty12 or '-', data_style)
                    month_count -= 1
                    month = (start_date - relativedelta(months=month_count)).month
                    if month_count == 0:
                        break

                worksheet.write(row, 26, row_total_amount, data_style)
                worksheet.write(row, 25, row_total_qty, data_style)
                row += 1
                tmp1 = tmp2 = tmp3 = tmp4 = tmp5 = tmp6 = tmp7 = tmp8 = tmp9 = tmp10 = tmp11 = tmp12 = 0
                tmp_qty1 = tmp_qty2 = tmp_qty3 = tmp_qty4 = tmp_qty5 = tmp_qty6 = tmp_qty7 = tmp_qty8 = tmp_qty9 = tmp_qty10 = tmp_qty11 = tmp_qty12 = 0
                row_total_qty = 0
                row_total_amount = 0
                

            worksheet.write(row, 0, "Total", column_heading_style)
            worksheet.col(25).width = 4000
            worksheet.col(26).width = 6000

            qty_total = jan_qty + feb_qty + mar_qty + apr_qty + may_qty + jun_qty + jul_qty + aug_qty + sep_qty + oct_qty + nov_qty + dec_qty
            amount_total = jan + feb + mar + apr + may + jun + jul + aug + sep + octo + nov + dec

            worksheet.write(row, 1, jan_qty, column_heading_style)
            worksheet.write(row, 3, feb_qty, column_heading_style)
            worksheet.write(row, 5, mar_qty, column_heading_style)
            worksheet.write(row, 7, apr_qty, column_heading_style)
            worksheet.write(row, 9, may_qty, column_heading_style)
            worksheet.write(row, 11, jun_qty, column_heading_style)
            worksheet.write(row, 13, jul_qty, column_heading_style)
            worksheet.write(row, 15, aug_qty, column_heading_style)
            worksheet.write(row, 17, sep_qty, column_heading_style)
            worksheet.write(row, 19, oct_qty, column_heading_style)
            worksheet.write(row, 21, nov_qty, column_heading_style)
            worksheet.write(row, 23, dec_qty, column_heading_style)
            worksheet.write(row, 25, qty_total, column_heading_style)

            worksheet.write(row, 2, jan, column_heading_style)
            worksheet.write(row, 4, feb, column_heading_style)
            worksheet.write(row, 6, mar, column_heading_style)
            worksheet.write(row, 8, apr, column_heading_style)
            worksheet.write(row, 10, may, column_heading_style)
            worksheet.write(row, 12, jun, column_heading_style)
            worksheet.write(row, 14, jul, column_heading_style)
            worksheet.write(row, 16, aug, column_heading_style)
            worksheet.write(row, 18, sep, column_heading_style)
            worksheet.write(row, 20, octo, column_heading_style)
            worksheet.write(row, 22, nov, column_heading_style)
            worksheet.write(row, 24, dec, column_heading_style)
            worksheet.write(row, 26, amount_total, column_heading_style)

            prepare = 'Prepared By:..................................'
            name = 'Name           :..................................'
            approve = 'Approved By:..................................'

            worksheet.row(row + 2).height_mismatch = True
            worksheet.row(row + 2).height = 450
            worksheet.row(row + 3).height_mismatch = True
            worksheet.row(row + 3).height = 450

            worksheet.write_merge(row + 2, row + 2, 2, 5, prepare,
                                  easyxf('font:height 200;font:bold True;align: horiz left,vertical center;'))
            worksheet.write_merge(row + 3, row + 3, 2, 5, name,
                                  easyxf('font:height 200;font:bold True;align: horiz left,vertical center;'))
            worksheet.write_merge(row + 2, row + 2, 22, 25, approve,
                                  easyxf('font:height 200;font:bold True;align: horiz left,vertical center;'))
            worksheet.write_merge(row + 3, row + 3, 22, 25, name,
                                  easyxf('font:height 200;font:bold True;align: horiz left,vertical center;'))

            fp = io.BytesIO()
            workbook.save(fp)
            excel_file = base64.encodestring(fp.getvalue())
            wizard.sale_report_region_file = excel_file
            wizard.file_name = 'Sale Report by Region.xls'
            wizard.sale_report_region_printed = True
            fp.close()
            return {
                'view_mode': 'form',
                'res_id': wizard.id,
                'res_model': 'sale.report.region',
                'view_type': 'form',
                'type': 'ir.actions.act_window',
                'context': self.env.context,
                'target': 'new',
            }
