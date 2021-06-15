{
    'name': 'Albarán UTE',
    'version': '14.0.1.0',
    'category': 'Documentation',
    'description': u"""

""",
    'author': 'Serincloud',
    'depends': ['repair','purchase_repair', ],
    'data': [
        #'security/ir.model.access.csv',
        'views/templates.xml',
        'views/albaran_ute_report.xml',
        'data/paper_ute.xml',
        'data/sequence.xml',
        'views/views.xml',
        #'views/views_menu.xml',
    ],
    'installable': True,
}
