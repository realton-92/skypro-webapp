# app.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Отправляем заголовок ответа
        self.send_response(200)
        # Указываем тип контента, как того требует задание
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Читаем содержимое HTML-файла "Контакты"
        try:
            with open('templates/contacts.html', 'rb') as file:
                html_content = file.read()
            self.wfile.write(html_content)
        except FileNotFoundError:
            # Если файл не найден, отправляем ошибку
            self.wfile.write(b"Error: contacts.html not found.")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Функция для запуска сервера."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на порту {port}")
    print(f"Перейдите по адресу: http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()