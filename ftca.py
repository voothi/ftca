from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import os
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Current working directory: {os.getcwd()}")
        with open('index.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('127.0.0.1', 5010)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running at http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
