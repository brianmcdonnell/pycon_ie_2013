#! /usr/bin/env python
import tornado.ioloop
import tornado.web
from tornado.options import options, define

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello from Tornado")

application = tornado.web.Application([
    (r"/hello", HelloHandler),
])

define('listen_address', group='webserver', default='127.0.0.1', help='Listen address')
define('listen_port', group='webserver', default=8080, help='Listen port')
define('unix_socket', group='webserver', default=None, help='Path to unix socket to bind')

if __name__ == "__main__":
    if options.unix_socket:
        from tornado.netutil import bind_unix_socket
        from tornado.httpserver import HTTPServer
        server = HTTPServer(application)
        socket = bind_unix_socket(options.unix_socket)
        server.add_socket(socket)
    else:
        application.listen(options.listen_port, address=options.listen_address)
    tornado.ioloop.IOLoop.instance().start()
