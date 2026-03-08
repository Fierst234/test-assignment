import http.server
import socketserver

PORT = 8080
RESPONSE = b"Hello from Effective Mobile!"


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(RESPONSE)))
            self.end_headers()
            self.wfile.write(RESPONSE)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[backend] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"[backend] Serving on port {PORT}")
        httpd.serve_forever()