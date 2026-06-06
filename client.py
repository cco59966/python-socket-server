import socket
import sys
import struct


def main():
    
    # total arguments
    n = len(sys.argv)
    if n < 4:
        print("Total arguments passed:", n)
        return
    
    host = sys.argv[1]
    port = (int (sys.argv[2]))
    filename = sys.argv[3]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        s.send(filename.encode('ascii'))

        outputData = s.recv(1024)
        
        print('Received from server repr:', repr(outputData))

        print('Received from server bytes:', outputData.decode('utf-8'))

        #msg = struct.unpack("!s", outputData)[0]
        #print("msg: ", msg)

        ans = input('Do you want to continue (y/n): ')
        if ans.lower() != 'y':
            break

    s.close()

if __name__ == '__main__':
    main()