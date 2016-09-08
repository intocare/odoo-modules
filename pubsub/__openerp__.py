# -*- coding: utf-8 -*-
{
	'name': "pubsub",
	'summary': """Publish changes of a model to an external API""",
	'description': """
		Notify an external API if a model changes
	""",
	'author': "Pridiktiv",
	'website': "http://pridiktiv.care",
	'license': "Other OSI approved licence",
	'category': 'Technical Settings',
	'version': '0.0',
	'depends': ['base'],
	'data': [
		'views/header.xml',
		'views/type.xml',
		'views/pubsub.xml'
	],
	'demo': [],
	'installable': True
}
