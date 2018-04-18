# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo import api


class City(models.Model):
    _name = 'res.country.city'
    _description = 'City'
    _order = 'name'

    name = fields.Char("Name", required=True, translate=True)
    zipcode = fields.Char("Zip")
    state_id = fields.Many2one(
        'res.country.state', 'State')


