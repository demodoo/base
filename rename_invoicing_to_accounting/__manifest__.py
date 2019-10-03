# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Rename Invoicing to Accounting",
    'version': '11.0.1.0.0',
    'summary': """Rename the Invoicing main menu to Accounting.""",
    'category': 'Accounting',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'account',
    ],
    'data': [
        'views/account_views.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}