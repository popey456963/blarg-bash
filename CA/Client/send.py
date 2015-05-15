import socket
import sys

HOST, PORT = "localhost", 9998
data = "Example,Data,For,Use,By,Me"
for i in range(1000):

        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        sock.close()
        
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))