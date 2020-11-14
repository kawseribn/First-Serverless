from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        output= {'female':'আবরেশমী শাহেদ'}
        json1=json.dumps(output,,ensure_ascii=False)
        message = json.loads(json1)
        self.wfile.write(message['female'].encode())
        return
