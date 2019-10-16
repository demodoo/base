# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class Meeting(models.Model):

    _inherit = 'calendar.event'

    name = fields.Char(translate=True)
