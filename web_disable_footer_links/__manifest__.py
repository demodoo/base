# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Web Disable Footer Links",
    'version': '11.0.1.0.0',
    'summary': """This module removes the links to 'Database Manager' and 'Powered by Odoo' in the login page""",
    'category': 'Website',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'web',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}