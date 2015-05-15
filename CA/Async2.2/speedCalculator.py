#!/usr/bin/python
# -*- coding: utf-8 -*-
#Calculate average speed in one really nice line
def avgspeed(time, distance):
    return str(float(distance)/(float(time)/3600))
#Return whether person is speeding or not
def speeding(speed, speedlimit):
    speed, speedlimit = float(speed), float(speedlimit)
    if speed > speedlimit:
        return "True"
    else:
        return "False"