from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain; charset=utf-8')
        self.end_headers()
        output= {'female':'কনিকা সাদিয়া'}
        message=json.dumps(output,ensure_ascii=False)
        self.wfile.write(message.encode('utf-8'))
        return
