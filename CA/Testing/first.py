import re, csv, sys, socket, socketserver, time

def Parser(data):
    datastr = data.decode("utf-8")
    dataarray = datastr.split(",")
    Handler(dataarray)
    pass

def Handler(data):
    #print("----------------------------------------")
    print("---------------Car Number " + data[0] + "---------------")
    print("Registration: " + data[1])
    print("Time (secs):  " + data[2])
    print("Distance:     " + data[3])
    print("Speed Limit:  " + data[4])
    print("Car Owner:    " + data[5] + "\n")
    RegistrationChecker(data[1])
    SpeedLimitChecker(int(data[4]))
    IntegerChecker(data[0],data[2],data[3],data[4])
    AvgSpeed(data[0],data[1],data[2],data[3],data[4],data[5])

def RegistrationChecker(registration):
    m = re.search('[A-Za-z]{2}[0-9]{2}[A-Za-z]{3}', registration)
    if m: pass
    else: print("Registration Test Failed \n")

def SpeedLimitChecker(speedlimit):
    if 0 < speedlimit or speedlimit > 200: pass
    else: print("Speed Test Failed \n")

def IntegerChecker(a,b,c,d):
    try:
        a,b,c,d=int(a),int(b),int(c),int(d)
    except:
        print("Integer Test Failed \n")

def AvgSpeed(index,reg,endtime,distance,speedlimit,name):
    time=float(endtime)/3600
    avgspeed=float(distance)/float(time)
    if avgspeed>float(speedlimit):
        print(name + " has broken the speed limit")
        highspeed = True
    else:
        print(name + " has not broken the speed limit")
        highspeed = False
    WriteResults(index,reg,endtime,distance,speedlimit,name,avgspeed,highspeed)

def WriteResults(a,b,c,d,e,g,h,i):
    with open('results.csv','a') as f:
        f.write('Index is: '+str(a)+','+
                'Registration is: '+str(b)+','+
                'Endtime is: '+str(c)+','+
                'Distance is: '+str(d)+','+
                'Speedlimit is: '+str(e)+','+
                'Name of Driver is: '+str(g)+','+
                'Average Speed is: '+str(h)+',' +
                'Is Speeding is: '+str(i)+'\n')
    
        
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        #print(self.client_address[0] + " wrote: " + str(self.data))
        # just send back the same data
        self.request.sendall(self.data)
        Parser(self.data)
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print("Server up and running!\n")
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()