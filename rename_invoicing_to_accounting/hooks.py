# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
import os
import base64
from odoo import SUPERUSER_ID
from odoo.api import Environment

logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    env = Environment(cr, SUPERUSER_ID, {})
    base_lang_import_model = env['base.language.import']

    for lang in [['es', 'es_ES'], ['de', 'de_DE'], ['en', 'en_US'], ['en_GB', 'en_GB'], ['fr', 'fr_FR'],
                 ['it', 'it_IT'], ['pt', 'pt_PT']]:
        iso_code = lang[0]
        code = lang[1]
        lang_file = open('%s/i18n/%s.po' % (path, iso_code), 'rb')
        file_data = lang_file.read()
        lang_file.close()

        wiz = base_lang_import_model.create({
            'name': iso_code,
            'code': code,
            'overwrite': True,
            'filename': '%s.po' % iso_code,
            'data': base64.b64encode(file_data)
        })
        wiz.import_lang()
        logger.info('Loaded %s language' % code)

    logger.info('post_init_hook executed! ;)')
