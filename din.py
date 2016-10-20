# din.py

import falcon
import festival
import json

from subprocess import call

class MessageResource(object):
	def on_post(self, req, resp):
		"""Handles POST requests"""
		body = req.stream.read()
		if not body:
			raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')
		msg = json.loads(body.decode('utf-8'))

		if 'stretchFactor' in msg:
			festival.setStretchFactor(msg['stretchFactor'])

		festival.sayText(msg['text'])

		resp.status = falcon.HTTP_200
		resp.body = ("hello")

app = falcon.API()

message = MessageResource()

app.add_route('/message', message)
