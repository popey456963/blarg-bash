from speed import *
from check import *
from csvwrite import *

def parse(response):
    #print('["Index", "Registration", "Time", "Distance", "Speedlimit", "Name"]')
    result = response.split(",")
    result.append(avgspeed(result[2], result[3]))
    result.append(speeding(result[6], result[4]))
    result.append(registration(result[1]))
    if result[8] == "False":
        csvwriter(result, "wrongreg")
    if result[7] == "True":
        csvwriter(result, "wrongspd")
        
    result[6] = str(round(float(result[6])))
    
    print("=============Car Number " + result[0] + "=============")
    #print("Registration: " + result[1])
    #print("Time:         " + result[2])
    #print("Distance:     " + result[3])
    #print("Speedlimit:   " + result[4])
    #print("Name:         " + result[5])
    #print("Avg Speed:    " + result[6])
    #print("Is Speeding:  " + result[7])
    #print("Registration: " + result[8]) 
    
    