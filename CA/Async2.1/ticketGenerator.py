#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv, os

mdarray = []

def rsendspeedsetup():
    with open("./names/names.txt", "r") as f:
        array = f.readlines()
    for i in array:
        mdarray.append(i.split("|"))
rsendspeedsetup()

def findvalue(name):
    passed = False
    for i in range(len(mdarray)):
        if mdarray[i][0] == name:
            mdarray[i][1] = int(mdarray[i][1]) + 1
            passed = True
    return(passed)
        
def updatenames():
    for i in range(len(mdarray)):
        mdarray[i][1] = str(mdarray[i][1])
        mdarray[i] = "|".join(mdarray[i])
    os.remove("names/names.txt")
    with open("names/names.txt", "a") as fil:
        for i in range(len(mdarray)):
            fil.write(mdarray[i])