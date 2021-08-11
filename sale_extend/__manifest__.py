# -*- coding: utf-8 -*-
{
    'name': "Sale Order Extend",

    'summary': """To show last sale price in sale order form""",

    'description': """
        To show last sale price in sale order form
    """,

    'author': "Asia Matrix Software Solution",

    'website': "http://www.asiamatrixsoftware.com",

    'category': 'Sale',

    'version': '1.2',

    'depends': [
        'sale',
        'hr',
        'sample_give_form',
    ],

    'data': [
        'reports/sale_issues_report.xml',
        'reports/stock_sale_reports.xml',
        'reports/sale_issue_report_template.xml',
        'reports/sale_report_template_extend.xml',
        'reports/stock_sale_delivery_report_template.xml',
        'reports/stock_sale_return_report_template.xml',
        'views/account_move_views.xml',
        'views/sale_extend_views.xml',
        'views/stock_views.xml',
    ],

    'installable': True,

    'application': False,
}