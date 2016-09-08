# -*- coding: utf-8 -*-

import re
from openerp import models, fields, api, exceptions

class HeaderField(models.Model):
	_name = 'pubsub.headerfield'

	name = fields.Char(string='Name', required=True)
	header_ids = fields.One2many('pubsub.header', 'field_id', string='Headers')

	# Set the SQL Constraints
	_sql_constraints = [
		('name_unique', 'UNIQUE(name)', 'The name must be unique')
	]

	@api.constrains('name')
	def _check_name(self):
		for r in self:
			if re.match('^[a-zA-Z0-9\-]+$', r.name) == None:
				raise exceptions.ValidationError('Invalid header name')
