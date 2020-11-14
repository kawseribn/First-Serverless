from http.server import BaseHTTPRequestHandler
from cowpy import cow
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        output= {'female':'আবরেশমী শাহেদ'}
        json1=json.dumps(output)
        message = json.loads(json1)
        self.wfile.write(message['female'].encode('utf-8'))
        return
