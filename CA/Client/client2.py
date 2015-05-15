import socket
import sys
import random
import time

l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = 0

def Caller():
    for i in range(99999):
        x = random.randint(1,100)
        if x < 75:
            rg(100)
        elif x < 80:
            rg(0)
        elif x < 85:
            rg(1)
        else:
            rg(100)
        #time.sleep(random.random()/2)

#Generate Valid Work
def rg(a):
    global index
    index = index + 1
    if a == 0: registration = random.choice(l) + random.choice(l) + str(random.randint(1,9)) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l)
    else: registration = random.choice(l) + random.choice(l) + str(random.randint(1,9)) + str(random.randint(1,9)) + random.choice(l) + random.choice(l) + random.choice(l)
    time = random.randint(1,20000)
    distance = random.randint(1,100)
    if a == 1: speedlimit = random.randint(1,100000)
    else: speedlimit = random.randint(1,100)
    name = random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l)
    string = str(index)+','+registration+','+str(time)+','+str(distance)+','+str(speedlimit)+','+name
    #print(string)
    send(string)

def send(MESSAGE):
    #HOST AND PORT
    HOST, PORT = "localhost", 9999
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(MESSAGE, "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()  
    print("Sent:     {}".format(MESSAGE))
    #print("Received: {}".format(received))
    if MESSAGE == received:
    #    print("The data matched\n")
        pass
    else:
        print("The data did not match\n")
