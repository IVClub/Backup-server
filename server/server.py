# First try to setup a for loop that echos back a message
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()



def main():
    Port = 8000
    server = HTTPServer(('',Port), helloHandler)
    print("server is running on port %s" % Port)
    server.serve_forever()




