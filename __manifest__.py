# -*- coding: utf-8 -*-
{
    'name': "last cost",
    'description': """
        Exemax custom
    """,

    'author': "Exemax",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase','stock','product_ux','sales_team','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
