# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Menuitem External Id",
    'version': '11.0.1.0.0',
    'summary': """The aim of this module is to facilitate to a developer the identification of 
    the external id of a menuitem. This module adds a new field to the ir.ui.menu model 
    with the external id of the menuitem.""",
    'category': 'Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'base',
    ],
    'data': [
        'views/ir_ui_menu_views.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
