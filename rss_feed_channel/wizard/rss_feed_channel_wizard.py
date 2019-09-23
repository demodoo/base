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
        rss_channel_list = self.env['mail.channel'].search([('rss_feed', '!=', '')])
        for rss_channel in rss_channel_list:
            feed_items = feedparser.parse(rss_channel.rss_feed)
            partners = rss_channel.message_partner_ids
            entries = feed_items.entries
            i = min(rss_channel.max_post-1, len(entries)-1)
            while i >= 0:
                post = entries[i]
                msgs = self.env['mail.message'].search([('body', 'ilike', '%'+post.link+'%')])
                i = i - 1
                if not msgs:
                    message = self.env['mail.message'].create({
                        'subject': rss_channel.name,
                        'subtype_id': 1,
                        'message_type': 'comment',
                        'body': "<p>%s <a target='_blank' href='%s'>%s</a></p>" % (post.title, post.link, post.link),
                        'record_name': rss_channel.name,
                        'email_from': self.env.user.email,
                        'reply_to': self.env.user.email,
                        'model': 'mail.channel',
                        'res_id': rss_channel.id,
                        'no_auto_thread': False,
                    })
                    partners.with_context(auto_delete=True)._notify(message, force_send=True, send_after_commit=False,
                                                                    user_signature=True)
