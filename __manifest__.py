# -*- coding: utf-8 -*-
{
    'name': "INDOGUNA GROUP - INVENTORY ",

    'summary': """
        INDOGUNA GROUP - INVENTORY  """,

    'description': """
        INDOGUNA GROUP - INVENTORY 
    """,

    'author': "Indoguna Utama, Andy Utomo",
    'website': "http://www.indoguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'security/user_groups.xml',
        'views/warehouse_views.xml',
        'views/opname_views.xml',
        'views/item_views.xml',
        'menu/menu.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}