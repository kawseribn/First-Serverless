from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        output= {'female':'আবরেশমী শাহেদ'}
        message=json.dumps(output,ensure_ascii=False)
        message=message.encode('utf-8')
        self.wfile.write(message)
        return
