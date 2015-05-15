#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Import all the other scripts
from speedCalculator import *
from regChecker import *
from fileWriter import *
from ticketGenerator import *

#Define parsing function
def parse(response):
    #Split into an array
    result = response.split(",")
    #Append the result of avgspeed
    result.append(avgspeed(result[2], result[3]))
    #Append the result of speeding
    result.append(speeding(result[6], result[4]))
    #Append whether the registration is correct
    result.append(registration(result[1]))
    #Test whether the registration is correct
    if result[8] == "False":
        #Write to a CSV name wrongreg
        csvwriter(result, "wrongreg")
    #Test whether speed is correct
    if result[7] == "True":
        #Write to a CSV name wrongspd
        csvwriter(result, "wrongspd")
        #Find value in the array
        findvalue(result[5])
    #Change result[6] to be an int (remove decimals)
    result[6] = str(round(float(result[6])))