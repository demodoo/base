# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _

class Channel(models.Model):

    _inherit = 'mail.channel'

    rss_feed = fields.Char('RSS Feed', default='', help="URL of the RSS Feed.")
    max_post = fields.Integer('Max Post', default=0, help="Max. number of items. 0 = All items.")
    contains = fields.Char('Contains', default='', help="Select items containing this text in "
                                                        "the title, in the url or in the description.")
    create_lead = fields.Boolean('Create a Lead/Opportunity', default=False, help="Check it to create a lead/opportunity, "
                                                                      "otherwise uncheck it.")
    team_id = fields.Many2one('crm.team', string='Sales Channel', help='Sale channel for the lead/opportunity.')
    activate = fields.Boolean('Activate', default=True, help="Check it to process the RSS Feed, "
                                                             "otherwise uncheck it.")

