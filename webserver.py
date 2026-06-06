# This here will import the  socket 
from socket import *  # This imports all of the  classes and all of the functions from the socket module to turn on network communication using sockets.

import sys  # In order to terminate this program
#  imports the sys, which  will allow the programs to terminate using sys.exit() when it is truly needed.

# Prepares now a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)  # This  is what creates a TCP server socket using the  IPv4 addressing.
serverSocket.bind(('localhost', 8089))  # This  will bind the server socket to the  local host on port 8089. So it can listen for  the connections that are incoming.
serverSocket.listen(5)  # the server socket,  which is implemented to have a maximum 5 connections
# This makes the server socket to now listen for the  incoming connection requests,  with a backlog pof 5 qued connections.

while True:
    # This here establishes the connection.
    print('Ready to serve...')  # This  will prints a message showing that the server is ready to accept and  also handle a connection.
    connectionSocket, addr = serverSocket.accept()  # This  accepts an incoming connection and returns a  new socket for the connection  along with the client address.

    try:
        message = connectionSocket.recv(1024).decode()  # This will now receive up to 1024 bytes from the client, decodes  from bytes to a now string, and it will store it within an variable message.
        print("Received message:\n", message)  # This prints an received HTTP request message.

        # Checks to see if the request is allowed or not
        if len(message.split()) > 1:  # This checks to see if the received message has more than one part when  it is  split by  the spaces showing  a new valid HTTP request.
            filename = message.split()[1]  # This takes out  the requested file path from the HTTP  request by takingg the second element after splitting.
            f = open(filename[1:])  
            # This opens  a new requested file for reading, it will also  remove the leading '/' from the filename to matchh the local file system.

            outputData = f.read()  # This reads all of the content of the requested file and it will alsoo store it in the variable  called outputData.

            # Sends the  HTTP  to the header's line
            connectionSocket.send(b'HTTP/1.1 200 OK\r\n')  # This sends the HTTP  about 200 OK response header to the client which would mean a successful request.
            connectionSocket.send(b'Content-Type: text/html\r\n')  # This will send  a header meaning and showingg that the content type is HTML.
            connectionSocket.send(b'\r\n')  #  this is the end of header
            # This  now sends an empty line to show  the end of the headers of HTTP.

            # Here sends the content of the requested file to the client.
            for i in range(len(outputData)):  # This would iterate over each character within the  outputData to send it character to character to the client.
                connectionSocket.send(outputData[i].encode())  # Here  encodes each character to bytes and sends it over the connection to the client.
            connectionSocket.send(b"\r\n")  # This sends a newline at the end of the file transfer.

            connectionSocket.close()  # This closes the connection socket after the file has been sent to the client.
        else:
            print("Invalid or empty request received, closing connection.")  # This prints a message indicating that an invalid or empty request was received.
            connectionSocket.close()  # This closes the connection socket since  the request was invalid or empty.
            continue  # This continues to the next iteration in order to wait for a new client connection.

    except IOError:
        # Sends  a response message noting file not found
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n')  # This will  send aa 404  NotFound HTTP response header for the  client if the wanted file is not  found.
        connectionSocket.send(b'Content-Type: text/html\r\n')  # This  will now send a header meaning that the content type of the response is HTML.
        connectionSocket.send(b'\r\n')  # This sends an empty line which will show  the end of the HTTP headers.
        connectionSocket.send(b'<html><body><h1>404 Not Found</h1></body></html>\r\n')  # This  here  will send a HTML body with a 404 Not Found message for   the client.

        # Closes the  client socket
        connectionSocket.close()  # This  will close the connection socket after it  sends an 404 response message to the client.

serverSocket.close()  # This closes the server socket when the server is terminating, releasing the port and resources.
sys.exit()  # This here will terminate the program after it  sends the corresponding data.
# This  will also terminate the program to make sure it exits it after sends the response data.
