#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}

HTTPServer.allow_reuse_address = True


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            json_response = json.dumps(python_dict)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            self.wfile.write(json_response.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            error = 'json {"error": "404 Not Found"}'
            self.send_response(404)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            self.wfile.write(error.encode("utf-8"))


PORT = 8000
with HTTPServer(("", PORT), Handler) as httpd:
    print("Serve on port 8000...")
    httpd.serve_forever()
