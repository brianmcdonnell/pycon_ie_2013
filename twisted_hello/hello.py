#! /usr/bin/env python
import argparse
import signal

from twisted.web import server
from twisted.internet import reactor
from txroutes import Dispatcher

class Greeting(object):
    def hello(self, request):
        return "Hello from Twisted (via txroutes)"

if __name__ == "__main__":
    def customHandler(signum, stackframe):
        reactor.stop()
    signal.signal(signal.SIGINT, customHandler)

    parser = argparse.ArgumentParser(description='Run the twisted hello server.')
    parser.add_argument('-c', '--connection', dest='connection', action='store', default='tcp', choices=('tcp', 'unix'), help='Use TCP or Unix connection')
    parser.add_argument('-s', '--sock-file', dest='sock_file', action='store', default='/tmp/twisted_hello.sock', help='')
    parser.add_argument('-i', '--interface', dest='interface', action='store', default='127.0.0.1', help='The interface to listen on')
    parser.add_argument('-p', '--port', type=int, dest='port', action='store', default=8080, help='The port to listen on')
    parser.add_argument('-b', '--backlog-size', type=int, dest='backlog_size', action='store', default=64, help='The socket listen backlog')
    args = parser.parse_args()

    dispatcher = Dispatcher()
    dispatcher.connect(name='test_hello', route='/hello', controller=Greeting(), action='hello')

    if args.connection.lower() == 'tcp':
        reactor.listenTCP(args.port, server.Site(dispatcher), args.backlog_size, interface=args.interface)
        print "Listening on http://%s:%s" % (args.interface, args.port)
    else:
        reactor.listenUNIX(args.sock_file, server.Site(dispatcher), wantPID=True)
        print "Listening on unix:%s" % args.sock_file
    reactor.run()

