from http.server import BaseHTTPRequestHandler
import json
import random as rand
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain; charset=utf-8')
        self.end_headers()
        output= {'female': 'কনিকা সাদিয়া'}
        json1=json.dumps(output,ensure_ascii=False)
        message=json.loads(json1)
        self.wfile.write(message['female'].encode('utf-8'))
        return
