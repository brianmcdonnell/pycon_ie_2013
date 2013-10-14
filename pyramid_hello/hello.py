#! /usr/bin/env python
from pyramid.response import Response
from pyramid.config import Configurator

def aview(request):
    return Response('Hello from Pyramid')

config = Configurator()
config.add_route('hello', '/hello')
config.add_view(aview, route_name='hello')
application = config.make_wsgi_app()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8080, application)
    print "Listening on http://0.0.0.0:8080"
    server.serve_forever()
