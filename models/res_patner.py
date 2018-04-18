from odoo import api,models,fields

class Partner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('res.country.city', string = 'City')
    district_id = fields.Many2one('res.country.district', string = 'District')

    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id:
            return {'domain': {'district_id': [('city_id', '=', self.city_id.id )]}}
        else:
            return {'domain': {'district_id': []}}

    @api.onchange('state_id')
    def _onchange_state_id(self):
        self.city_id = None
        self.district_id = None
        if self.state_id:
            return {'domain': {'city_id': [('state_id', '=', self.state_id.id)]}}
        else:
            return {'domain': {'city_id': []}}

