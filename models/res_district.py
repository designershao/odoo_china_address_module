# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class District(models.Model):
    _name = 'res.country.district'
    _description = 'District'
    _order = 'name'

    name = fields.Char("Name", required = True)
    city_id = fields.Many2one(
        'res.country.city', 'City'
    )
