print('Initializing sensor calibration')
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, MoveDifferential, SpeedRPM
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.wheel import EV3Tire
from time import time



colSFollower = ColorSensor(INPUT_1)
colSCrossDetect = ColorSensor(INPUT_2)
stopButton = TouchSensor(INPUT_3)

print('Initializing finished')

while(True):
    print(colSCrossDetect.reflected_light_intensity<15,colSFollower.reflected_light_intensity<15)

  

