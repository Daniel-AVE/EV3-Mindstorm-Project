#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

cd = ColorSensor(port=Port.S1)
conveyer = Motor(Port.A)
receptor = Motor(Port.B)


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

color_to_box_position = {"red":1,"white":2,"blue":3,"black":4}
pokerchip_count = {"red":0,"white":0,"blue":0,"black":0}
value = {"red":10, "white":20, "blue":50, "black":100}

previous_box_position = 2
pot = 0
conveyer.run(100)
while True:
  
    chip = ReadColor(cd.rgb())
    if chip != "conveyer":
        wait(200)
        if chip == ReadColor(cd.rgb()):
            print(chip)
            pokerchip_count[chip] += 1
            pot += value[chip]
            box_shift = color_to_box_position[chip]-previous_box_position
            receptor.run_target(100, receptor.angle()+30*box_shift)
            previous_box_position = color_to_box_position[chip]
            wait(1000)

#Red 16 4 8
#White 44 47 86
#Blue 4 8 24
#Black 4 4 6
#Conveyer 0 0 3