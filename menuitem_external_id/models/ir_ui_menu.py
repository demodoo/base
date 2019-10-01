# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class IrUiMenu(models.Model):

    _inherit = 'ir.ui.menu'

    ext_id = fields.Char('External Id', default='', compute='_compute_ext_id', search='_search_ext_id',
                         help="External Id of the menuitem.")

    def _compute_ext_id(self):
        for record in self:
            menu_obj_l = self.env['ir.model.data'].sudo().search([('res_id', '=', record.id),
                                                                   ('model', '=', 'ir.ui.menu')], limit=1)
            if menu_obj_l:
                menu_obj = menu_obj_l[0]
                record.ext_id = '%s.%s' % (menu_obj.module, menu_obj.name)
            else:
                record.ext_id = ''

    def _search_ext_id(self, operator, value):
        domain = [('model', '=', 'ir.ui.menu'), '|', ('name', operator, value), ('module', operator, value)]
        data = self.env['ir.model.data'].sudo().search(domain)
        return [('id', 'in', data.mapped('res_id'))]
