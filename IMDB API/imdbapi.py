import requests, json, sys
from tabulate import tabulate

def imdb(name):
  data = requests.get('http://www.omdbapi.com/?t=' + name).text
  jdata = json.loads(data)
  p = []
  [p.extend([k,v]) for k,v in jdata.items()]
  return(p)
  
def printData():
    print("--" + sys.argv[1] + "--")
    for i in var:
        if i[0] == "Genre":
            print("Genre: " + i[1])
        if i[0] == "Plot":
            print("Plot: " + i[1])

filmdata = imdb(sys.argv[1])
counter = -1
var = []

for i in range(len(filmdata)):
    if i % 2 == 0:
        counter = counter + 1
        var.append([filmdata[i], filmdata[i+1]])

#print(tabulate(var))

#printData()