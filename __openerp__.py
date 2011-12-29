# -*- coding: utf-8 -*-

{
    "name": "Price Unit on Stock Move ",
    "version": "1.01",
    "depends": ["product", "stock"],
                    "author": "C & G Software S.a.s.",
    "category": "Stock",
    "description": """ Visualizza nei Picking e in stock move 
    """,
    "init_xml": [],
    'update_xml': [
                   'stock_view.xml',
                   'security/ir.model.access.csv',
                   ],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': '${certificate}',
}
