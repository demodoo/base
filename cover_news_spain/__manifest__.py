# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Cover News of Spain",
    'version': '11.0.1.0.0',
    'summary': """This module allows to follow easily the cover news of Spain. It uses 
    our rss_feed_channel module. News can be readed in the Discuss menu.""",
    'category': 'Extra Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'rss_feed_channel',
    ],
    'data': [
        'data/mail_channel.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}