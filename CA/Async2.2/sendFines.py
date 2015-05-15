#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Variables
filelocation = "./names/names.txt"
lineno = 0
#Replace specific line with specific text
def replace_line(line_num, text):
    #Read lines
    with open(filelocation, 'r') as file:
        lines = file.readlines()
        #Change specific line
        lines[line_num] = text
    #Write changed line
    with open(filelocation, 'w') as file:
        file.writelines(lines)
#Read file
with open(filelocation, "r") as file:
    #For every line, split it into another array (multi-dimensional array)
    #It's a CSV seperated by pipes (which makes it not a CSV, but hey...)
    for line in file:
        line = line.split("|")
    
        #Means that they actually speeded!
        if int(line[1]) > 0:
            print("Send a ticket to " + line[2].strip() + " with a price of £" + str(int(line[1]) * 20))
            #Open output file and write that they have speeded.  Include some data.
            with open("speeders.txt", "a") as file:
                file.write(line[2].strip() + "|" + str(int(line[1]) * 20) + "\n")
            #Remove all outstanding speeding tickets
            replace_line(lineno, line[0] + "|" + "0" + "|" + line[2])
        #Increase lineno by one.
        lineno = lineno + 1
            
