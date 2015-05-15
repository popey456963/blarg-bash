#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

mdarray = []
"""
def replace_line(line_num, text):
    lines = open("./names/names.txt", 'r').readlines()
    lines[line_num] = text
    out = open("./names/names.txt", 'w')
    out.writelines(lines)
    out.close()

def sendspeed(name):
    #First, find the position in the file
    #Uhm, before that, read the file.
    with open("./names/names.txt", 'r') as file:
        lineno = 0
        for line in file:
            if name in line:
                #print(line.strip())
                line = line.split("|")
                line[1] = str(int(line[1]) + 1)
                line = "|".join(line)
                replace_line(lineno, line)
            lineno = lineno + 1
"""            
def rsendspeedsetup(): #Faster SendSpeed Function
    with open("./names/names.txt", "r") as f:
        array = f.readlines()
    for i in array:
        mdarray.append(i.split("|")) #We now have an array of items
rsendspeedsetup()

#So, array of wonderful items.  It should look something like:
"""
NAME TICKETS ADDRESS
AAAA 0       AGJORF
AAAB 0       GNREOL
"""
def findvalue(name):
    passed = False
    for i in range(len(mdarray)):
        if mdarray[i][0] == name:
            mdarray[i][1] = int(mdarray[i][1]) + 1
            passed = True
    return(passed)
        
#Now just to find a way to make it update names.txt with the new thing
def updatenames():
    for i in range(len(mdarray)):
        mdarray[i][1] = str(mdarray[i][1])
        mdarray[i] = "|".join(mdarray[i])
    with open("names/names2.txt", "a") as fil:
        for i in range(len(mdarray)):
            fil.write(mdarray[i])