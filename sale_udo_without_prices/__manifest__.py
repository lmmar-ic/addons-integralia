{
    'name': 'Sale Order for Udo and Without Prices',
    'version': '14.0.1.0',
    'category': 'Ventas',
    'description': u"""

""",
    'author': 'Serincloud',
    'depends': ['sale', 'sale_udo', 'report_qweb_pdf_watermark' ],
    'data': [
        'views/sale_udo_without_prices.xml',
        'views/templates.xml',
    ],
    'installable': True,
}
