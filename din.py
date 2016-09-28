# din.py 

import falcon
import festival

from subprocess import call

class MessageResource(object):
	def on_post(self, req, resp):
		"""Handles POST requests"""
		body = req.stream.read()
		msg = body.decode('utf-8')

		festival.sayText(msg)

		resp.status = falcon.HTTP_200
		resp.body = ("hello")
		

app = falcon.API()

message = MessageResource()

app.add_route('/message', message)
