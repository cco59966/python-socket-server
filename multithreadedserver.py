import socket  # This  will import the socket module which will  enable  the  network communication using the  sockets.

from _thread import start_new_thread  # This will  import the start_new_thread function from the thread module, which will  create new threads for handling clients.
import threading  # This here  imports the threading  to use  of  locks for  the synchronization between  the threads.

lock = threading.Lock()  # This  will create a Lock object named 'lock' which will be in usee to synchronize access to shared resources across the  threads.

 def handle_client(c):  # This defines the function handle_client, which will handle new client connections using the socket 'c'.
    while True:  # Here starts what will be an   loop that is inifite  in order to continuously handle the  requests from the  connected  client.
        filename = c.recv(1024)  # This gets about 1024 bytes of data from the client socket, which were expecting to be an filename requested.
     print('inbound filename:', filename)  # This  here prints  the received filename used for debugging and logging purposes.
         if not filename:  #   here sees if the filename  wreceived is empty or None, meaning that the client has closed the connection.
            print('Good Bye: no file name to load')  # This here  prints a  message saying goodbye which means no filename  has been received.
             lock.release()  # here  releases the previously acquired lock to allow other threads to proceed.
            break  # This breaks out of the loop, ending the handling of this client connection.

        f = open(filename[0:])  # This opens the requested file  using the filename received from the client.
         outputData = f.read()  # it will  reads the enti re content of the opened file and stores it in the variable outputData.
         print(outputData)  # This prints the contents of the file to the console for debugging and v snd also for verifications.
        outMsg = bytes(outputData, 'utf-8')  # This encodes the string data in outputData into bytes using  the UTF8 encoding, storing it in outMessage.
        c.send(outMsg)  # This sends the file's  encoded  data back to the client over  connection.

    c.close()  # This  will close the client socket  after the loop ends, whichwill terminate the connection with the client.

def main():  #  Dmakes the main function which  will  set up the server and  also will manage new client connections.
    host = ''  # This also makes the host  to an empty string so  thatt the server will now listen on all available interfaces.
    port = 8089  # here  sets the port number that the  the serverr will listen on to 8089.
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # This  develops  a TCP socket using the  IPv4 addressing i believe.
    s.bind((host, port))  # This will binds the socket to the  host and port so that it can listen for more new connections.
    s.listen(5)  # Here sets the socket  so that it will  listen for newconnections and also it  allows up to 5 queued connections requests.
    print("Server running on port", port)  # This prints a message n making sure the server is running and also is  listening on the specific port noted.

    while True:  #  starts a infinite loop  looking to accept and handle new  client connections continuously.
        c, addr = s.accept()  #  Creates a new client connection making  the client socket c and the client address addr.
        lock.acquire()  #  Gets the the lock to make sure the  thread is  handling  before starting a new thread for the client.
        print('Connected to:', addr[0], ':', addr[1])  #  also this prints the IP address and port number of the connected client for logging.
        start_new_thread(handle_client, (c,))  # Now starts a new thread to handle the client connection using the handle_client function, passing the client socket as an argument.

if __name__ == '__main__':  #  checks to see if the script is being run as the main program.
    main()  # This calls the main function to start the server and  also it will begin listening for connections.
