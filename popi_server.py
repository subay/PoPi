#import sys

#from gevent.wsgi import WSGIServer

from popi import app


#if __name__ == '__main__':
#    http_server = WSGIServer(("127.0.0.1", 5050), app)
#    try:
#        http_server.serve_forever()
#    except KeyboardInterrupt:
#        print "Stopping web server"
#        sys.exit(0)

if __name__ == '__main__':
    app.run()