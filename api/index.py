from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        output= {'female':'kawser'}
        message=json.dumps(output,ensure_ascii=False)
        self.wfile.write(message.encode())
        return
