{
    'name': 'test_module',
    'application': True,
    'installable': True,
    'sequence': 1,
    'depends': ['base'],

'data': [
    'security/ir.model.access.csv',
    'views/test_model_views.xml',
    'wizard/wizard_model_view.xml',
    ]
}