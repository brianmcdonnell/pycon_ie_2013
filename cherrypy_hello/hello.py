#! /usr/bin/env python

import cherrypy
cherrypy.log.access_file = None

class Handler:
  @cherrypy.expose
  def hello(self):
    r = cherrypy.response
    r.headers['Content-Type'] = 'text/plain'
    return "Hello from CherryPy"

application = cherrypy.Application(Handler(), '/cherrypy_hello', None)

if __name__ == "__main__":
    import cherrypy.wsgiserver
    wsgi_application = cherrypy.Application(Handler(), '/', None)
    listen_cfg = ('127.0.0.1', 8000)
    server = cherrypy.wsgiserver.CherryPyWSGIServer(listen_cfg, wsgi_application, 1)
    print "Cherrypy listening on http://%s:%s" % listen_cfg
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
