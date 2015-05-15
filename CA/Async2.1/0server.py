#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket, sys, threading, socketserver, random, time

from setupSystem import *
from testargs import *

carryon = True
index = 0
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = testFile("./names/names.txt", "Names File")
p = testargs(sys.argv)

print("==============Testing Initiated==============")
print(testFolder("./names", "Names Folder"))
print(testFolder("./wrong", "Wrong Folder"))
print(x)
print(p)
print("==============Testing Finished===============")

if p == "Testing Args .......................... False":
    carryon = False
    print("No Arguments were given!  Stopping D:")
    print("Example usage is `python3 0server.py 1000000`")
if x == "Checking Names File ................... False":
    import namesGenerator
    
from mainFile import *

def generator():
    global index
    index = index + 1
    registration = random.choice(l) + random.choice(l) + str(random.randint(1,9)) + str(random.randint(1,9)) + random.choice(l) + random.choice(l) + random.choice(l)
    time = random.randint(1,20000)
    distance = random.randint(1,100)
    speedlimit = random.randint(1,100)
    name = random.choice(l) + random.choice(l) + random.choice(l)
    string = str(index)+','+registration+','+str(time)+','+str(distance)+','+str(speedlimit)+','+name
    return string

def update_progress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...         \r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "="*block + " "*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


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

if __name__ == "__main__"  and carryon:
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start on e
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    numbers = int(sys.argv[1])
    start_time = time.time()
    for i in range(numbers):
        update_progress(i/numbers)
        text = generator()
        try:
            client(ip, port, text)
        except:
            pass
    updatenames()
    update_progress(1)
    runtime = time.time() - start_time
    print("Runtime (s): " + str(runtime))
    print("Registrations: " + str(numbers))
    print("Calcs per Sec: " + str(round(numbers/runtime)))

    server.shutdown()
    from sendFines import *