#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from operator import itemgetter

files = os.listdir("./wrong")

for items in range(len(files)):
    
    print("Opened " + files[items])
    
    with open('./wrong/' + files[items]) as fin:
        lines = [line for line in fin]
        lines = lines[:-1]
        
    lines.sort(key=itemgetter(1))
    with open('./wrong/' + files[items], 'w') as fout:
        for el in lines:
            fout.write(el)
