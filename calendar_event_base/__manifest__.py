# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Calendar Event Base",
    'version': '11.0.1.0.0',
    'summary': """This module makes several changes to the calendar module. See the README file for detailed changes.""",
    'category': 'Extra Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'web',
        'calendar',
    ],
    'data': [
        'views/calendar_event_views.xml',
    ],
    'qweb': [
        'static/src/xml/web_calendar.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
