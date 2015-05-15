#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Imports
import socket
import sys
import threading
import socketserver
import random
import time

#Variables
carryon = True
index = 0
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arrays = []
#How many times to repeat it
numbers = int(sys.argv[1])

#Run and take functions from setup and mainFile
from setup import *
from mainFile import *

#Generate data
def generator():
    array = []
    array.append(str(index + 1))
    array.append(random.choice(l) + random.choice(l) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + random.choice(l) + random.choice(l) + random.choice(l))
    array.append(str(random.randint(1, 20000)))
    array.append(str(random.randint(1, 100)))
    array.append(str(random.randint(1, 100)))
    array.append(random.choice(l) + random.choice(l) + random.choice(l))
    #Multidimensional array
    arrays.append(array)

#Progress bar, credit to Brian Khuu, changed slightly to be more compact.
def progress(progress):
    barLength, status = 20, ""
    if type(progress) is int:
        progress = float(progress)
    if progress >= 1:
        progress = 1
        status = "Done...                        \r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [" + "="*(block) + " "*(barLength-block) + "] " + str(progress*100) + "% " + status
    sys.stdout.write(text)
    sys.stdout.flush()

#From here on it's an asynchrous socket server from the Python wiki
#Allows speed
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
        #Parse the response
        parse(response)
    finally:
        sock.close()

if __name__ == "__main__" and carryon:
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    #Generate all the data
    for i in range(numbers):
        generator()
    #Start timer
    start_time = time.time()
    #For all numbers...
    for i in range(numbers):
        #Set percentage
        progress(i/numbers)
        try:
            #Attempt to send array to the client function
            client(ip, port, ",".join(arrays[i]))
        except:
            #If fails, continue, but print to output
            pass
            print("Error :(")
    #Get endtime
    end_time = time.time()
    #Work out the runtime
    runtime = end_time - start_time
    #Make sure progress bar has updated correctly, fails at some numbers otherwise
    progress(1)
    #Update names (calculate the tickets to send out)
    updatenames()

    #Print runtime values
    print("Runtime (s): " + str(runtime))
    print("Registrations: " + str(numbers))
    print("Calcs per Sec: " + str(round(numbers/runtime)))
    #Shutdown server
    server.shutdown()
    #Actually send the tickets
    from sendFines import *
