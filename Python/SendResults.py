import urllib2
path = ""
with open('file.txt') as f:
    path = f.readlines()[-1]


def send():
    global send, path
    path = "http://www.hacker.org/runaway/index.php?name=popey456963&password=password123&path=" + path
    results = urllib2.urlopen(path).read()
    print "Level Complete!"
    
send()