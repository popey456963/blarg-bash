#!/usr/bin/python
# -*- coding: utf-8 -*-
def avgspeed(time, distance):
    return str(float(distance)/(float(time)/3600))

def speeding(speed, speedlimit):
    speed, speedlimit = float(speed), float(speedlimit)
    if speed > speedlimit:
        return "True"
    else:
        return "False"