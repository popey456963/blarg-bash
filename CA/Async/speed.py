def avgspeed(time, distance):
    time = float(time) / 3600
    speed = float(distance)/time
    return str(speed)
    
def speeding(speed, speedlimit):
    speed, speedlimit = float(speed), float(speedlimit)
    if speed > speedlimit:
        return "True"
    else:
        return "False"