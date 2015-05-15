#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Import necessary OS tools to find path
import os.path
#Define function for data and datapath
def csvwriter(data, datapath):
    #Define path
    path = "./wrong/" + datapath + data[1][0] + ".txt"
    #See whether file exists
    fileexists = os.path.isfile(path) 
    #It dosen't, create it and add headings.
    if not fileexists:
        #With means I don't need to close it
        with open(path, "a") as file:
            file.write("No.|Registration|Time|Distance|Speedlimit|Name|AvgSpeed|IsSpeeding|Registration|EOL\n")
    #With means I don't need to close it        
    with open(path, "a") as file:
        #Iterate throguh all the data
        for i in range(len(data)):
            #Write the data seperated by pipe symbols
            file.write(data[i] + "|")
        #Write EOL to designate the end of the line.  \n is an escape character
        file.write("EOL\n")