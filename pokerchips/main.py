#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

cd = ColorSensor(port=Port.S1)

color_values = {"red":(16,4,8),"white":(44,47,86),"blue":(4,8,24),"black":(4,4,6),"conveyer":(0,0,3)}

def dist(coord1, coord2):
    return abs(((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2 + (coord2[2]-coord1[2])**2)**(1/2))

def ReadColor(coordinate):
    return_color = "error"
    distance = 100
    for key in color_values:
        new_distance = dist(coordinate,color_values[key])
        if new_distance < distance:
            return_color = key
            distance = new_distance 
    return return_color


while True:
    print(ReadColor(cd.rgb()))
    wait(100)
#Red 16 4 8
#White 44 47 86
#Blue 4 8 24
#Black 4 4 6
#Conveyer 0 0 3