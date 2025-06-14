# RESTful API

This document explains the structure of HTTP requests and responses, the differences between HTTP and HTTPS, and status code categories.

---

## Difference Between HTTP and HTTPS

- **HTTP** does not encrypt its data, so anyone can read it.
- **HTTPS** adds a layer of encryption, so data can't be read easily.

---

## HTTP Request Structure

1. Request Line  
   - Example: `GET /index.html HTTP/1.1`  
   - Contains: method (GET), path (resource), HTTP version (1.1)

2. Headers  
   - Example: `Host: www.example.com`  
   - Key-value pairs with info like browser type, accepted formats

3. Blank Line  
   - A single blank line to separate headers from the body

4. Body (optional)  
   - Only present in some requests (e.g. POST, PUT)  
   - Contains data sent to server

**Example:**
POST /submit-form HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

name=Alice&email=alice@example.com

---

## HTTP Response Structure

1. Status Line  
   - Example: `HTTP/1.1 200 OK`  
   - Contains: HTTP version, status code, status message

2. Headers  
   - Example: `Content-Type: text/html`  
   - Key-value pairs like content type, length, server info

3. Blank Line  
   - A single blank line separates headers from the body

4. Body (optional)  
   - The actual content sent back (HTML, JSON, image, etc.)

**Example:**
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 70

<html>
  <body>
    <h1>Hello, Alice!</h1>
  </body>
</html

---

## Status Code
| Status Code | Category         | Meaning                                                    |
|-------------|------------------|------------------------------------------------------------|
| 1xx         | Informational    | Request received, continuing process                       |
| 2xx         | Successful       | Request successfully processed                             |
| 3xx         | Redirection      | Further action needs to be taken                           |
| 4xx         | Client Errors    | The request has an error or cannot be fulfilled (e.g., page not found) |
| 5xx         | Server Errors    | The server failed to complete a valid request              |


