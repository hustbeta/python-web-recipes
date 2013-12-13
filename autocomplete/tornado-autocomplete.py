#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os.path
import random
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class AutoCompleteHandler(tornado.web.RequestHandler):
    def get(self):
        term = self.get_argument('term')
        response = []
        for i in range(4):
            response.append(term + str(random.random())[2:])
        self.write(tornado.escape.json_encode(response))
	self.set_header('content-Type', 'application/json')

if __name__ == '__main__':
    settings = {'static_path': os.path.dirname(__file__)}
    application = tornado.web.Application([('/', IndexHandler), ('/autocomplete', AutoCompleteHandler)], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
