{
    'name': 'Albarán UTE',
    'version': '14.0.1.0',
    'category': 'Documentation',
    'description': u"""

""",
    'author': 'Serincloud',
    'depends': ['purchase_repair',
                'purchase_so',
                'sale_management',],
    'data': [
        #'security/ir.model.access.csv',
        'views/templates.xml',
        'views/albaran_ute_report.xml',
        'data/sequence.xml',
        'views/views.xml',
        #'views/views_menu.xml',
    ],
    'installable': True,
}
