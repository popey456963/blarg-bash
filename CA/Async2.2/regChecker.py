#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Import regex
import re
#Function that takes in the registration
def registration(registration):
    #Get first seven chars - make sure it's not a longer string like AA11AAAB - which would work otherwise
    #Also stops BAA11AAA ;)
    registration = registration[:7]
    #Test if registration is in there
    m = re.match('[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{3}', registration)
    #If m is there, it's right :)
    if m: 
        return "True"
    #It's not right if it gets to here.  M was not found
    else: 
        return "False" # Incorrect Registration