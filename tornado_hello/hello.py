#! /usr/bin/env python
import tornado.ioloop
import tornado.web
from tornado.options import options, define

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello from Tornado")

application = tornado.web.Application([
    (r"/hello", HelloHandler),
], debug=False)

define('listen_address', default='127.0.0.1', help='Listen address')
define('listen_port', default=8080, help='Listen port')
define('unix_socket', default=None, help='Path to unix socket to bind')
define('backlog_size', default=8191, help='Size of the listen backlog')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    if options.unix_socket:
        from tornado.netutil import bind_unix_socket
        from tornado.httpserver import HTTPServer
        server = HTTPServer(application)
        socket = bind_unix_socket(options.unix_socket, backlog=options.backlog_size)
        server.add_socket(socket)
        print "Listening on %s" % options.unix_socket
    else:
        application.listen(options.listen_port, address=options.listen_address)
        print "Listening on http://%s:%s" % (options.listen_address, options.listen_port)

    tornado.ioloop.IOLoop.instance().start()
