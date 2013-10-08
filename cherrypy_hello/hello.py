#! /usr/bin/env python

import cherrypy

class Handler:
  @cherrypy.expose
  def index(self):
    r = cherrypy.response
    r.headers['Content-Type'] = 'text/plain'
    return "Hello from CherryPy"

def application(environ, start_response):
  cherrypy.tree.mount(Handler(), '/hello', None)
  return cherrypy.tree(environ, start_response)

if __name__ == "__main__":
    cherrypy.quickstart(Handler(), '/hello', None)
