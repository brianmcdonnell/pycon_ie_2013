#! /usr/bin/env python

import cherrypy

class Handler:
  @cherrypy.expose
  def hello(self):
    r = cherrypy.response
    r.headers['Content-Type'] = 'text/plain'
    return "Hello from CherryPy"

application = cherrypy.Application(Handler(), '/', None)

if __name__ == "__main__":
    import cherrypy.wsgiserver
    server = cherrypy.wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8000), application, 1)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
