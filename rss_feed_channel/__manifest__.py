# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "RSS Feed channel",
    'version': '11.0.1.1.0',
    'summary': """This module allows to define RSS feeds through discussion channels. This module allows 
    to follow easily in Odoo the latest updates (news, videos, ...) of your favourite RSS feeds. Also, it can 
    generate leads/opportunities from the feed items.""",
    'category': 'Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'mail',
        'crm'
    ],
    'data': [
        'data/ir_cron.xml',
        'views/mail_channel_views.xml',
    ],
    'qweb': [
        'static/src/xml/thread.xml'
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
