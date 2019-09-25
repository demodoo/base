# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
import feedparser
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class RSSFeedChannelWizard(models.TransientModel):
    _name = 'rss.feed.channel.wiz'

    @api.model
    def process_rss_feed_channels(self):
        rss_channel_list = self.env['mail.channel'].search([('rss_feed', '!=', ''), ('activate', '=', True)])
        for rss_channel in rss_channel_list:
            feed_items = feedparser.parse(rss_channel.rss_feed)
            partners = rss_channel.message_partner_ids
            text = rss_channel.contains or ''
            entries = feed_items.entries
            i = min(rss_channel.max_post-1, len(entries)-1)
            if i == -1:
                i = len(entries)-1
            while i >= 0:
                post = entries[i]
                i = i - 1
                if text == '':
                    cond = True
                else:
                    title = str(post.title)
                    link = str(post.link)
                    description = str(post.description)
                    cond = title.find(text) != -1 or \
                           link.find(text) != -1 or \
                           description.find(text) != -1
                if cond:
                    msgs = self.env['mail.message'].search([('body', 'ilike', '%'+post.link+'%')])
                    if not msgs:
                        message = self.env['mail.message'].create({
                            'subject': rss_channel.name,
                            'subtype_id': 1,
                            'message_type': 'comment',
                            'body': "<p><strong>%s</strong><br/>%s <a target='_blank' href='%s'>%s</a></p>" %
                                    (post.title, post.description, post.link, post.link),
                            'record_name': rss_channel.name,
                            'email_from': self.env.user.email,
                            'reply_to': self.env.user.email,
                            'model': 'mail.channel',
                            'res_id': rss_channel.id,
                            'no_auto_thread': False,
                        })
                        partners.with_context(auto_delete=True)._notify(message, force_send=True, send_after_commit=False,
                                                                        user_signature=True)
                        if rss_channel.create_lead:
                            #Create a lead/opportunity
                            team_id = rss_channel.team_id
                            self.env['crm.lead'].create({
                                'name': post.title,
                                'partner_id': self.env.user.partner_id.id,
                                'user_id': None,
                                'team_id': team_id.id,
                                'description': "<p><strong>%s</strong><br/>%s <a target='_blank' href='%s'>%s</a></p>" %
                                    (post.title, post.description, post.link, post.link),
                                'referred': self.env.user.partner_id.name
                            })
