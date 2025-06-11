#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}
info_dict = {"version": "1.0",
             "description": "A simple API built with http.server"}

# set the class attribute allow_reuse_address to True, so the server can immediately reuse the PORT after it's closed
HTTPServer.allow_reuse_address = True


# define a Handler class inheriting from BaseHTTPRequestHandler, to customize  how HTTP requests are handled
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            message = "Hello, this is a simple API!"
            # send the response status to 200 to indicate the request was successful
            self.send_response(200)
            # send an http header to specify the type of content being returned.
            self.send_header("Content-Type", "text/plain")
            # tell the server no more headers to be added
            self.end_headers()
            # write the response body, must be in bytes, encode("utf-8" converts str to bytes)
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


# Workflow
"""
1, Check the requested path: if self.path == ''

2, Prepare the response content

3, Send HTTP response status
   - Syntax: self.send_response(status)

4, Set HTTP response header
   - Syntax: self.send_header("Content-Type", "text/plain")
   - self: refers to the instance of HTTP request class(aseHTTPRequestHandler)
   - send_heander is a method provided by BaseHTTPRequestHandler to add single header line to the response
   - Parameters: first is header field name, second is header field value
                 which tells the user that the response body is plain text
              
5, End HTTP headers
   - Syntax: self.end_headers()

6, Write response body
   - Syntax: self.wfile.write(message.encode("utf-8"))
   - self.wfile: wfile is a file-like obj, which is used to write raw bytes back to user
   - self.wfile.write(...) writes the given data to the output stream, only bytes allowed
   - message.encode("utf-8"): converts str to bytes using UTF-8 encoding
"""
