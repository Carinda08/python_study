import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = "./web"
port = 80

if len(sys.argv) > 1:
    webdir = sys.argv[1]

if len(sys.argv) > 2:
    port = int(sys.argv[2])

print ("webdir <%s>,  port <%s>" % (webdir, port))

os.chdir(webdir)
svraddr = ("", port)
svrobj = HTTPServer (svraddr, CGIHTTPRequestHandler)
svrobj.serve_forever()
