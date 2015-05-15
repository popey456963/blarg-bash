import re, urllib2, time, threading, itertools
password = "password123"
hackerpath = "http://www.hacker.org/runaway/index.php?name=popey456963&password=" + password
source = urllib2.urlopen(hackerpath).read().splitlines()
result = '\n'.join(item for item in source if '<PARAM NAME=FlashVars VALUE="FVterrainString=' in item)
result = result.split("&")

rmapdata = result[0].split("=")[3]
rmax = result[1].split("=")[1]
rmin = result[2].split("=")[1]
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

for x in range(int(rmax)-int(rmin)):
    values = itertools.combinations_with_replacement('RD', x+int(rmin))
for item in values:
    print item