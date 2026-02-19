{
    'name': 'POS eTIMS Auto Invoice',
    'version': '15.0.1.0.0',
    'category': 'Point of Sale',
    'author': 'Morris-Kinyua',
    'website': 'https://wa.me/2547105050561',
    'support': 'https://wa.me/2547105050561',
    'license': 'OPL-1',
    'price': 100.00,
    'currency': 'USD',
    'summary': 'Automatically create posted and paid invoices with eTIMS integration for POS orders',
    'description': """
        This module automatically creates posted and paid invoices when the validate button 
        is clicked in POS with the invoice option selected. After posting, it triggers 
        the eTIMS integration to generate invoices with eTIMS details on both the invoice 
        form and report document.
    """,
    'depends': ['point_of_sale', 'account', 'l10n_ke_etims_vscu'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}