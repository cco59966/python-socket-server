# python-socket-server
 TCP client-server implementation in Python featuring a multithreaded file server and a basic HTTP web server built from scratch using raw sockets.

# Python Socket Server

A networking project built from scratch in Python using raw sockets, 
demonstrating client-server architecture, HTTP request handling, and 
multithreaded connections — without relying on any web frameworks.

## Components

### Web Server (webserver.py)
A basic HTTP/1.1 server that:
- Listens for incoming browser or client connections on port 8089
- Parses HTTP GET requests and extracts the requested filename
- Serves HTML files with proper HTTP response headers
- Returns a 404 Not Found response if the requested file doesn't exist

### Multithreaded File Server (multithreadedserver.py)
A TCP file server that:
- Handles multiple clients simultaneously using Python threads
- Uses a threading lock to synchronize shared resource access
- Reads and sends file contents back to connected clients
- Gracefully handles client disconnections

### TCP Client (client.py)
A TCP client that:
- Connects to a running server by host, port, and filename
- Sends file requests and prints the server's response
- Supports multiple requests in a single session

## Tech Stack

- Language: Python
- Networking: Python socket module (raw TCP/IP)
- Concurrency: Python threading, _thread
- Protocol: HTTP/1.1

## Getting Started

**Requirements:** Python 3.x

**Run the web server:**
```bash
python3 webserver.py
```
Then open your browser and navigate to:
