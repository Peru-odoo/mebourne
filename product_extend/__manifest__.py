# -*- coding: utf-8 -*-
{
    'name': "Product Extend",
    'summary': """
        Add Product Attributes""",
    'description': """
        Add Product Consumption,Shape and Type
    """,
    'author': "Asiamatrix",
    'website': "http://www.asiamatrixsoftware.com",
    'category': 'Product',
    'version': '0.8',
    'depends': ['product','sale','product_brand','multi_branches'],
    'data': [
        'views/product_category.xml',
        'views/sale_order_line_view.xml',
        'views/purchase_request_view.xml',
    ],
}