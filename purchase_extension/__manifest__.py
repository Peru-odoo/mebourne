{
    'name':
    'Purchase Extension',
    'sequence':
    3,
    'version':
    '13.1.9',
    'description':
    'Purchase Request Form and Invoice Format Extension',
    'summary':
    "Calculation of usage per day for purchase's products and format design for request form.",
    'category':
    'Purchase',
    'depends': ['purchase', 'purchase_stock', 'partner_code_generate'],
    'data': [
        'views/action_manager.xml',
        'wizard/po_list_by_vendor_wizard.xml',
        'wizard/po_payable_receivable_wizard.xml',
    ],
    'installable':
    True,
    'application':
    True,
    'license':
    'OPL-1',
    'author':
    'Matrix',
}
