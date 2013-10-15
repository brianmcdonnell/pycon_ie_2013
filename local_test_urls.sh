#!/bin/bash
echo ""
echo "--- NGINX ---"
curl http://localhost/hello
echo ""
curl http://localhost/a.gif
echo ""
echo ""
echo "--- SKELETON WSGI/PYTHON APPS ---"
curl http://localhost/http_hello
echo ""
curl http://localhost/fastcgi_hello
echo ""
curl http://localhost/uwsgi_hello
echo ""
curl http://localhost/uwsgi_unix_hello
echo ""
echo ""
echo "--- PYTHON WEB FRAMEWORKS ---"
curl http://localhost/django_hello/hello
echo ""
curl http://localhost/django_min_hello/hello
echo ""
curl http://localhost/flask_hello/hello
echo ""
curl http://localhost/bottle_hello/hello
echo ""
curl http://localhost/cherrypy_hello/hello
echo ""
echo ""
echo "--- PYTHON ASYNC WEB FRAMEWORKS ---"
curl http://localhost/twisted_hello/hello
echo ""
curl http://localhost/tornado_hello/hello
echo ""
echo ""
echo "--- OTHER ASYNC WEB FRAMEWORKS ---"
curl http://localhost/node_hello/hello
echo ""
curl http://localhost/go_hello/hello

