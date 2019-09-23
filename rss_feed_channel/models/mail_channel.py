# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _

class Channel(models.Model):

    _inherit = 'mail.channel'

    rss_feed = fields.Char('RSS Feed', default='')
    max_post = fields.Integer('Max Post', default=5)
