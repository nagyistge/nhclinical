# -*- encoding: utf-8 -*-
{
    'name': 'NH Clinical Core',
    'version': '0.1',
    'category': 'Clinical',
    'license': 'AGPL-3',
    'summary': '',
    'description': """    """,
    'author': 'Neova Health',
    'website': 'http://www.neovahealth.co.uk/',
    'depends': ['nh_activity', 'hr', 'nh_base'],
    'data': ['data/data.xml', 
             'views/pos_view.xml',
             'views/location_view.xml',
             'views/patient_view.xml',
             'views/user_view.xml',
             'views/device_view.xml',
             'views/operations_view.xml',
             'wizards/placement_wizard_view.xml',
             'views/menuitem.xml',
             'security/ir.model.access.csv',
             'security/adt/ir.model.access.csv',
             'security/operations/ir.model.access.csv'],
    'demo': [],
    'css': [],
    'js': [],
    'qweb': [],
    'images': [],
    'application': True,
    'installable': True,
    'active': False,
}