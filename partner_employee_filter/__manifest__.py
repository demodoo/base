# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Partner Employee Filter",
    'version': '11.0.1.0.0',
    'summary': """This module add a new employee filter in Contacts menu.""",
    'category': 'Hidden',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
