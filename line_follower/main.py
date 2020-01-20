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

leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C)

# diameter = 43 # mm
# axletrack = 145 # mm
# robot = DriveBase(leftmotor, rightmotor, diameter, axletrack)

c = ColorSensor(Port.S3)
t = TouchSensor(Port.S1)

SPEED = 150 # deg / second
MIDPOINT = 50
CORRECTION = -5
INTERVAL = 0.05 # seconds

while not t.pressed():
  cv = c.reflection()
  mismatch = cv - MIDPOINT
  direction = mismatch * CORRECTION
  if direction > SPEED:
    direction = SPEED
  if direction < -SPEED:
    direction = -SPEED

  print("Reflect: ", cv, ", Mismatch = ", mismatch, " -> Direction: ", direction)
  
  if direction < 0:
    leftmotor.run(SPEED)
    rightmotor.run(SPEED + direction)
  else:
    leftmotor.run(SPEED - direction)
    rightmotor.run(SPEED)

  time.sleep(INTERVAL)

leftmotor.stop()
rightmotor.stop()