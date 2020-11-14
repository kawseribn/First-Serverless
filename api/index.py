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
        import jsonwith open(self.json1) as f:  message = json.load(f)
        self.wfile.write(message.encode("utf-8"))
        return
