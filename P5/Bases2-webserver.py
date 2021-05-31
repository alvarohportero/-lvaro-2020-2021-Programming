import http.server
import socketserver
from pathlib import Path

IP = "127.0.0.1"
PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)

            content = Path("index.html").read_text()
        else:
            resource = self.path[1:]  # /info/A.html -> info/A.html
            print(f"Resource: {resource}")

            try:
                content = Path(resource).read_text()
                self.send_response(200)
            except FileNotFoundError:
                self.send_response(400)

                content = Path("Error.html").read_text()

        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(content, "utf-8"))


handler = TestHandler

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((IP, PORT), handler) as httpd:  # HTTP Daemon
    print(f"Serving at port {PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by the user")
