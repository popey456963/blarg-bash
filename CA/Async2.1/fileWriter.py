#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os.path
def csvwriter(data, datapath):
    path = "./wrong/" + datapath + data[1][0] + ".txt"
    fileexists = os.path.isfile(path) 
    if not fileexists:
        with open(path, "a") as file:
            file.write("No.|Registration|Time|Distance|Speedlimit|Name|AvgSpeed|IsSpeeding|Registration|EOL\n")
            
    with open(path, "a") as file:
        for i in range(len(data)):
            file.write(data[i] + "|")
        file.write("EOL\n")