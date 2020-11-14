from http.server import BaseHTTPRequestHandler
from cowpy import cow
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        output= {'male':'আবরেশমী শাহেদ'}
        json1=json.dumps(output)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = json1
        self.wfile.write(message.encode("utf-8"))
        return
