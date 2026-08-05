# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'estates',
    'depends' : [
	'base',
    ],
    'data' : [
        'security/ir.model.access.csv',

        'views/estates_properties_views.xml',
	    'views/estates_menus.xml',
    ],
}
