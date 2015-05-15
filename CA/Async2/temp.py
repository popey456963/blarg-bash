#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

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