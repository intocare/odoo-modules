# -*- coding: utf-8 -*-

import re
from openerp import models, fields, api, exceptions

class Subscription(models.Model):
	_name = 'pubsub.subscription'

	name = fields.Char(string='Name', required=True)
	url = fields.Char(string='Endpoint', required=True)
	description = fields.Text()
	header_ids = fields.One2many('pubsub.header', 'subscription_id', string='Headers')
	type_ids = fields.Many2many('pubsub.type', string='Types')

	# Set the SQL Constraints
	_sql_constraints = [
		('name_unique', 'UNIQUE(name)', 'The name must be unique')
	]

	@api.constrains('url')
	def _check_url(self):
		for r in self:
			if re.match('^(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?$', r.url) == None:
				raise exceptions.ValidationError('Invalid URL')

	@api.constrains('header_ids')
	def _check_headers(self):
		for r in self:
			headers = r.header_ids
			size = len(headers)

			# Running time: O(n^2)
			# TODO: Implemented with mergesort, running time will be reduced to O(n log(n))
			for i in range(0, size):
				for j in range(i+1, size):
					if headers[i].field_id.id == headers[j].field_id.id:
						raise exceptions.ValidationError('Duplicate header `{}`'.format(headers[i].field_id.name))
