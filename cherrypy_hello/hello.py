#! /usr/bin/env python
import cherrypy

# Disable logging by default
cherrypy.log.access_file = None
cherrypy.log.screen = False

class Handler:
  @cherrypy.expose
  def hello(self):
    r = cherrypy.response
    r.headers['Content-Type'] = 'text/plain'
    return "Hello from CherryPy"

application = cherrypy.Application(Handler(), '/cherrypy_hello', None)

if __name__ == "__main__":
    # Enable logging to screen when run from command line
    cherrypy.log.screen = True
    wsgi_application = cherrypy.Application(Handler(), '/', None)
    listen_cfg = ('127.0.0.1', 8000)
    import cherrypy.wsgiserver
    server = cherrypy.wsgiserver.CherryPyWSGIServer(listen_cfg, wsgi_application, 1)
    print "Cherrypy listening on http://%s:%s" % listen_cfg
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
