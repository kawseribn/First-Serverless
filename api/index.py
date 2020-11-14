from http.server import BaseHTTPRequestHandler
from cowpy import cow
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.output= {'male':'আবরেশমী শাহেদ'}
        self.json1=json.dumps(self.output)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = json.load(self.json1)
        self.wfile.write(message.encode())
        return
