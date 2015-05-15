import requests, json, sys, ast
from tabulate import tabulate

data = []

with open("output.txt", "r") as f:
    content = f.readlines()
    #print(content)
    
for b in content:
    b = b.split("`")
    data.append([b[0], b[1].split(",")[0], b[2]])

for item in data:
    if item[0][:3] == "[It":
        print("This item could not been found... (" + item[1] +")")
    else:
        print(item[0] + " - " + item[1])
    
    
    
#print(data)