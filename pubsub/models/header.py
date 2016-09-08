# -*- coding: utf-8 -*-

from openerp import models, fields

class Header(models.Model):
	_name = 'pubsub.header'

	field_id = fields.Many2one('pubsub.headerfield', ondelete='restrict', string='Field', required=True)
	value = fields.Char(string='Value', required=True)

	subscription_id = fields.Many2one('pubsub.subscription', ondelete='cascade', string='Subscription', required=True)
