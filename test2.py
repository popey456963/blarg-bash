import urllib2
while 1:
    path = "http://www.hacker.org/runaway/index.php?name=popey456963&password=" + "password123"
    results = urllib2.urlopen(path).read()
    print "Got One!"