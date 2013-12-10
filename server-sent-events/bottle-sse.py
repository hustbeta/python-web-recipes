#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import datetime
import time

@bottle.get('/')
def index():
    return bottle.static_file('index.html', root='.')

@bottle.get('/stream')
def stream():
    bottle.response.content_type = 'text/event-stream'
    bottle.response.cache_control = 'no-cache'

    while True:
        yield 'data: %s\n\n' % str(datetime.datetime.now())
        time.sleep(5)

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080, debug=True)
