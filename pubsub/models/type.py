# -*- coding: utf-8 -*-

from openerp import models, fields

class Type(models.Model):
	_name = 'pubsub.type'

	type = fields.Char(string='Type', required=True)

	# Set the SQL Constraints
	_sql_constraints = [
		('type_unique', 'UNIQUE(type)', 'The type must be unique')
	]
