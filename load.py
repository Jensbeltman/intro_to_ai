from time import sleep, time
from crossDetection import crossDetection
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, MoveDifferential, SpeedRPM
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.wheel import EV3Tire
from linefollower import LineFollower

# rightMotor = LargeMotor(OUTPUT_A)
# leftMotor = LargeMotor(OUTPUT_B)
# rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
# leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
mdiff = MoveDifferential(OUTPUT_B, OUTPUT_A, EV3Tire, 100)
