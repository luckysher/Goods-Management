# -*- coding: utf-8 -*-
{
    'name': "Goods-Management",
    'version': "1.1",
    'summary': """Managing Goods Simple""",
    'description': """
        The goods management app can help the users the manage their goods via orders, bills, invoices and
        tracking of goods etc.
     """,
    'author': "luckyshera",
    'website': "http://www.luckyshera.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
    ],
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}