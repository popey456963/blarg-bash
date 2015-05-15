import requests, json, sys
from tabulate import tabulate
from multiprocessing import Pool

def imdb(name):
  data = requests.get('http://www.omdbapi.com/?t=' + name).text
  jdata = json.loads(data)
  p = []
  [p.extend([k,v]) for k,v in jdata.items()]
  return(p)
  
def printData(title):
    try:
        for i in var:
            if i[0] == "Title":
                title = i[1]
                print("==Title: " + i[1] + "==")
        for i in var:
            if i[0] == "Genre":
                genre = i[1]
                print("Genre: " + i[1])
            if i[0] == "Plot":
                plot = i[1]
                print("Plot: " + i[1])
        with open("output.txt", "a") as f:
            f.write(str(title + "`" + genre + "`" + plot) + "\n")
    except:
        with open("output.txt", "a") as f:
            f.write("[Item could not be found: `" +  title.strip() + "`]\n")
        
            
with open("input.txt") as f:
    content = f.readlines()

def value(item):
    global var
    
    filmdata = imdb(item)
    counter = -1
    var = []

    for i in range(len(filmdata)):
        if i % 2 == 0:
            counter = counter + 1
            var.append([filmdata[i], filmdata[i+1]])

    #print(tabulate(var))
    
    printData(item)
    
#for item in content:
#    value(item)
    
if __name__ == '__main__':
    with Pool(5) as p:
        p.map(value, content)