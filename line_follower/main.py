#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Write your program here
brick.sound.beeps(1)

leftmotor = Motor (Port.B)
rightmotor = Motor (Port.C)

diameter = 43 # mm
axletrack = 145 # mm
robot = DriveBase (leftmotor, rightmotor, diameter, axletrack)

robot.drive(100, 0)
time.sleep(2)
robot.stop()