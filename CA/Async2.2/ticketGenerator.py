#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv, os
#MultiDimensionalARRAY
mdarray = []

#Improved name finding algorithm by caching items in array.
#Size even with large databases (12 mill in UK) is still small enough to run on 8GB of RAM
def rsendspeedsetup():
    #Open file
    with open("./names/names.txt", "r") as f:
        #Real all lines
        array = f.readlines()
    for i in array:
        #Split all files in array
        mdarray.append(i.split("|"))
#Run this on startup (this whoel thing gets run at start)
rsendspeedsetup()

#See if value actually exists
def findvalue(name):
    passed = False
    for i in range(len(mdarray)):
        if mdarray[i][0] == name:
            mdarray[i][1] = int(mdarray[i][1]) + 1
            passed = True
    return(passed)
        
#Update names
def updatenames():
    #For items
    for i in range(len(mdarray)):
        #Get number of crimes
        mdarray[i][1] = str(mdarray[i][1])
        #Join the array
        mdarray[i] = "|".join(mdarray[i])
    #Remove the file
    os.remove("names/names.txt")
    #Recreate it with new stuff
    with open("names/names.txt", "a") as fil:
        for i in range(len(mdarray)):
            fil.write(mdarray[i])