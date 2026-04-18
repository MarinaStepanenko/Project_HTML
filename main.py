from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_contacts_page(self):
        """Читает HTML-файл и возвращает его содержимое"""
        try:
            with open("contacts.html", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return """
            <!DOCTYPE html>
            <html>
            <head><title>Ошибка</title></head>
            <body>
                <h1>Файл contacts.html не найден!</h1>
                <p>Убедитесь, что файл находится в той же папке, что и сервер.</p>
            </body>
            </html>
            """

    def do_GET(self):
        """На ЛЮБОЙ GET-запрос возвращаем страницу Контакты"""
        # Неважно, какой адрес (self.path) — всегда показываем контакты
        page_content = self.__get_contacts_page()

        self.send_response(200)
        self.send_header("Content-type", "text/html")  # ← text/html, а не application/json
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")
    print("На любой GET-запрос будет показана страница Контакты")
    print("Для остановки сервера нажмите Ctrl+C")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")