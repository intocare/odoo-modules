# -*- coding: utf-8 -*-

import requests
import json
import copy
import logging
from openerp import models, fields, api

_logger = logging.getLogger(__name__)

class Data(models.Model):
	_name = 'pubsub.data'

	ref = fields.Id(string='Ref', required=True)
	type = fields.Char(string='Type', required=True)
	data = fields.Serialized(string='Data')

	def _get_headers(self, ids):
		record = self.env['pubsub.header'].search_read([('id', 'in', ids)])

		headers = {}

		# Iterate over the headers and add them to the object
		for header in record:
			headers[header.get('field_id')[1]] = header.get('value')

		# Set `Content-Type` to `application/json` regarding of what is set in the settings
		headers['Content-Type'] = 'application/json'

		return headers

	def _in_type_list(self, type, ids):
		# Check if the type is associated with the subscription
		length = self.env['pubsub.type'].search_count([('id', 'in', ids), ('type', '=', type)])

		return length > 0

	def _publish(self, vals):
		# Copy the `vals` object and change `ref` to `id`
		data = copy.copy(vals)
		data['id'] = data['ref']

		del data['ref']

		result = self.env['pubsub.subscription'].search_read([])

		for r in result:
			types = r.get('type_ids')

			if len(types) == 0 or self._in_type_list(data['type'], types):
				_logger.info('invoke')

				url = r.get('url')
				headers = self._get_headers(r.get('header_ids'))

				requests.post(url, headers=headers, data=json.dumps(data))

	@api.model
	def create(self, vals):
		rec = super(Data, self).create(vals)

		# Publish to all the subscriptions
		self._publish(vals)

		return rec

