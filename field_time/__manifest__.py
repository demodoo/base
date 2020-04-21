# -*- coding: utf-8 -*-
# Copyright 2020 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Datetime Time Field Widget",
    'version': '11.0.1.0.0',
    'summary': """A field widget to show only the time (hh:mm:ss) of a datetime field.""",
    'category': 'Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'base',
    ],
    'data': [
        'views/time_views.xml',
    ],
    'qweb': [
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
