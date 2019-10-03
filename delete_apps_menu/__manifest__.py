# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Delete Apps Menu",
    'version': '11.0.1.0.0',
    'summary': """Delete the Apps menu and its submenus.""",
    'category': 'Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'base',
        'web_settings_dashboard',
    ],
    'data': [
        'views/base_view.xml',
    ],
    'qweb': ['static/src/xml/dashboard.xml'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}