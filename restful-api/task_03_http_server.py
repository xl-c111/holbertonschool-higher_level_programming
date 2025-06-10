#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}
info_dict = {"version": "1.0",
             "description": "A simple API built with http.server"}

HTTPServer.allow_reuse_address = True


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            message = "Hello, this is a simple API!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            json_response = json.dumps(python_dict)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json_response.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == "/info":
            json_response = json.dumps(info_dict)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_response.encode("utf-8"))

        else:
            error = "Endpoint not found"
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(error.encode("utf-8"))


with HTTPServer(("", 8000), Handler) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
