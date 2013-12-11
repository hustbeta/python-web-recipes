#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('Welcome new user.')

    def on_close(self):
        print 'client closed', self

    def on_message(self, message):
        self.write_message(str(datetime.datetime.now()) + ': ' + message)
        print 'received:', message

if __name__ == '__main__':
    settings = {'static_path': os.path.dirname(__file__)}
    application = tornado.web.Application([('/', IndexHandler), ('/websocket', WSHandler)], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
