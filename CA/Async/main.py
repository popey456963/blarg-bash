import socket
import threading
import socketserver
from calculate import *
import random

index = 0
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generator():
    global index
    index = index + 1
    registration = random.choice(l) + random.choice(l) + str(random.randint(1,9)) + str(random.randint(1,9)) + random.choice(l) + random.choice(l) + random.choice(l)
    time = random.randint(1,20000)
    distance = random.randint(1,100)
    speedlimit = random.randint(1,100)
    name = random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l)
    string = str(index)+','+registration+','+str(time)+','+str(distance)+','+str(speedlimit)+','+name
    return string

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        self.request.sendall(bytes(data, 'ascii'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        #print("Received: {}".format(response))
        parse(response)
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    
    for i in range(99999):
        text = generator()
        client(ip, port, text)

    server.shutdown()