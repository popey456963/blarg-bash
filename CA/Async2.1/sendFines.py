#!/usr/bin/python3
# -*- coding: utf-8 -*-
filelocation = "./names/names.txt"
lineno = 0

def replace_line(line_num, text):
    with open(filelocation, 'r') as file:
        lines = file.readlines()
        lines[line_num] = text
        
    with open(filelocation, 'w') as file:
        file.writelines(lines)
    
with open(filelocation, "r") as file:
    for line in file:
        line = line.split("|")
    
        if int(line[1]) > 0:
            #print("Send a ticket to " + line[2].strip() + " with a price of £" + str(int(line[1]) * 20))
            with open("speeders.txt", "a") as file:
                file.write(line[2].strip() + "|" + str(int(line[1]) * 20) + "\n")
                
            replace_line(lineno, line[0] + "|" + "0" + "|" + line[2])
    
        lineno = lineno + 1
            
