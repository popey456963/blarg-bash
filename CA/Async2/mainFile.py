#!/usr/bin/python3
# -*- coding: utf-8 -*-
from speedCalculator import *
from regChecker import *
from fileWriter import *
from ticketGenerator import *

def parse(response):
    result = response.split(",")
    result.append(avgspeed(result[2], result[3]))
    result.append(speeding(result[6], result[4]))
    result.append(registration(result[1]))
    if result[8] == "False":
        csvwriter(result, "wrongreg")
    if result[7] == "True":
        csvwriter(result, "wrongspd")
        findvalue(result[5])
    result[6] = str(round(float(result[6])))