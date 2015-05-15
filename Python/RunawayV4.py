password = "password123"










































































import re, urllib2, time, threading

def 
    result = '\n'.join(item for item in urllib2.urlopen("http://www.hacker.org/runaway/index.php?name=popey456963&password=" + password).read().splitlines() if '<PARAM NAME=FlashVars VALUE="FVterrainString=' in item).split("&")
    
    rmax = result[1].split("=")[1]
    rmin = result[2].split("=")[1]
    rmapdata = result[0].split("=")[3]
    rlengthx = int(result[3].split("=")[1])
    rlengthy = int(result[4].split("=")[1])
    
    rmaptemp = re.findall("." * int(rlengthx),rmapdata)
    
    iterator = 0
    for items in rmaptemp:
        rmaptemp[iterator] = list(items)
        iterator = iterator + 1
    rmap = rmaptemp
    temparray = []
    for items in range(len(rmap)):
        rmap[items].append("G")
    for items in range(rlengthx):
        temparray.append("G")
    rmap.append(temparray)
    rx, ry = 0, 0
    
    def send(x):
        path = "http://www.hacker.org/runaway/index.php?name=popey456963&password=" + password + "&path=" + ''.join(x)
        results = urllib2.urlopen(path).read()
        print results
    
    print "Min Instrutions = " + rmin
    print "Max Instructions = " + rmax
    print "Map Data = " + rmapdata
    print "Length = [" + str(rlengthx) + ", " + str(rlengthy) + "]"
    print "============================Map=============================="
    print rmap    
    
    for i in range(pow(2, int(rmax))):
        x = list(bin(int(i))[2:])
        rx, ry = 0, 0
        for j in range(len(x)):
            if x[j] == "0": 
                x[j] = "R"
            if x[j] == "1": 
                x[j] = "D"
        y = x
        print x
        x = x * 100
        for i in x:
            if i == "R":
                rx = rx + 1
            if i == "D":
                ry = ry + 1
            print str(rx) + " " + str(ry)
            if rmap[ry][rx] == "X":
                break
            if rmap[ry][rx] == "G":
                print "Solution Found"
                print x
                send(y)