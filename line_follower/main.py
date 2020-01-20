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
CORRECTION = -7
INTERVAL = 0.05 # seconds

leftmotor.reset_angle(0)
rightmotor.reset_angle(0)

DIST = 2000

while not t.pressed() and (leftmotor.angle() + rightmotor.angle() < DIST):
  cv = c.reflection()
  mismatch = cv - MIDPOINT
  direction = mismatch * CORRECTION

  if direction > SPEED:
    over = direction - SPEED
    leftmotor.run(SPEED)
    rightmotor.run(-over)
  elif direction > 0:
    leftmotor.run(SPEED)
    rightmotor.run(SPEED - direction)
  elif direction > -SPEED:
    leftmotor.run(SPEED + direction)
    rightmotor.run(SPEED)
  else:
    over = direction + SPEED
    leftmotor.run(-SPEED - over)
    rightmotor.run(SPEED)

  print("Reflect: ", cv, ", Mismatch = ", mismatch, " -> Direction: ", direction)

  time.sleep(INTERVAL)

leftmotor.stop()
rightmotor.stop()

print("LEFT: ", leftmotor.angle())
print("RIGHT: ", rightmotor.angle())