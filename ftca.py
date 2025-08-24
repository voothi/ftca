from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import html
import base64
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        text_from_query = ''
        
        # НОВАЯ ЛОГИКА: Проверяем, есть ли параметр s_b64
        if 's_b64' in query_params:
            try:
                base64_string = query_params['s_b64'][0]
                base64_bytes = base64_string.encode('utf-8')
                # Декодируем из Base64 обратно в байты, а затем в строку UTF-8
                text_bytes = base64.b64decode(base64_bytes)
                text_from_query = text_bytes.decode('utf-8')
            except Exception as e:
                print(f"Ошибка декодирования Base64: {e}")
                text_from_query = "Ошибка декодирования текста."
        # Старая логика для обратной совместимости и простых тестов
        elif 's' in query_params:
            text_from_query = query_params.get('s', [''])[0]

        is_multiline = query_params.get('multiline', ['false'])[0].lower() == 'true'

        try:
            with open('index.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Error: index.html not found.")
            print(f"Error: index.html not found in current directory: {os.getcwd()}")
            return

        # Логика вставки текста остается прежней
        if is_multiline:
            safe_text = html.escape(text_from_query)
            html_content = html_content.replace('{TEXT_CONTENT}', safe_text)
        else:
            # Если это не multiline-запрос, то JS обработает параметр 's'
            html_content = html_content.replace('{TEXT_CONTENT}', '')


        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('127.0.0.1', 5010)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running at http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()