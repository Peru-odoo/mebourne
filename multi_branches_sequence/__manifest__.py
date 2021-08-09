# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Sequence",

    'summary': """Customer Invoice Sequence""",

    'description': """
        Customer Invoice Sequence By Branch.
    """,

    'author': "asiamatrix",

    'website': "http://www.asiamatrixsoftware.com",

    'category': 'Accounting',

    'version': '0.1',

    'depends': [
        'account',
        'sale',
        'purchase',
        'multi_branches',
    ],

    'data': [
        'views/branches_sequence.xml',
    ],
}