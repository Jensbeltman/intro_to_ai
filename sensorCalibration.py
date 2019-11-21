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
    stopButton.wait_for_pressed()
    stopButton.wait_for_released()
    wD = int(input('Type in distance between the wheels in mm'))
    mDiff = MoveDifferential(OUTPUT_B, OUTPUT_A, EV3Tire, wD)


    sensorValues = []

    mDiff.turn_left(5,360,block=False)
    t = time()
    while mDiff.is_running:
        sensorValues.append(colSFollower.reflected_light_intensity)
    mDiff.wait_until_not_moving()
    print("Run time",time()-t)

    maxVal = max(sensorValues)
    minVal = min(sensorValues)
    midVal = minVal+(maxVal-minVal)/2
    meanVal = sum(sensorValues)/len(sensorValues)
    print('nrVal','maxVal','minVal','midVal','meanVal')
    print(len(sensorValues),maxVal,minVal,midVal,meanVal)
    #print(sensorValues)

    stopButton.wait_for_pressed()
    stopButton.wait_for_released()

