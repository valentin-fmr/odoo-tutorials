# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperties(models.Model):
    _name = "estates.properties"
    _description = "Estate Properties Tutorials"
    
    name = fields.Char(required=True)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    availability = fields.Datetime(default=fields.Datetime.now)
    description = fields.Text()
    #garden_orientation = fields.Selection("north", "south", "east", "west",)
    state = fields.Selection(
        string='Status',
        required=True,
        copy=False,
        default='new',
        selection=[('new', 'New'), ('offer_received', 'Offer received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        help="Current status of property")

    active = fields.Boolean(default=True)

