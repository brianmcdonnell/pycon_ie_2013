#!/bin/bash
echo ""
echo "--- NGINX ---"
curl http://server.pycon.ie/hello
echo ""
curl http://server.pycon.ie/a.gif
echo ""
echo ""
echo "--- SKELETON WSGI/PYTHON APPS ---"
curl http://server.pycon.ie/http_hello
echo ""
curl http://server.pycon.ie/fastcgi_hello
echo ""
curl http://server.pycon.ie/uwsgi_hello
echo ""
curl http://server.pycon.ie/uwsgi_unix_hello
echo ""
echo ""
echo "--- PYTHON WEB FRAMEWORKS ---"
curl http://server.pycon.ie/django_hello/hello
echo ""
curl http://server.pycon.ie/django_min_hello/hello
echo ""
curl http://server.pycon.ie/flask_hello/hello
echo ""
curl http://server.pycon.ie/bottle_hello/hello
echo ""
curl http://server.pycon.ie/cherrypy_hello/hello
echo ""
echo ""
echo "--- PYTHON ASYNC WEB FRAMEWORKS ---"
curl http://server.pycon.ie/twisted_hello/hello
echo ""
curl http://server.pycon.ie/tornado_hello/hello
echo ""
echo ""
echo "--- OTHER ASYNC WEB FRAMEWORKS ---"
curl http://server.pycon.ie/node_hello/hello
echo ""
curl http://server.pycon.ie/go_hello/hello

