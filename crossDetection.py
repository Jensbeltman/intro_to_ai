

from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor 

colorSensorCenter = ColorSensor(INPUT_2)
colorSensorRight = ColorSensor(INPUT_1)

colorIntensCenter = colorSensorCenter.reflected_light_intensity
colorIntensRight = colorSensorRight.reflected_light_intensity

lightValue = 10

def crossDetected():

    if((colorIntensRight<=lightValue) and (colorIntensCenter<=lightValue)):
        retrunValue=1
    else:
        retrunValue=0

    return retrunValue


rightMotor = LargeMotor(OUTPUT_A)
leftMotor = LargeMotor(OUTPUT_D)
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
colorSensorCenter = ColorSensor(INPUT_2)



print('its me..')

speed = 50

#refTime = time()+20
#currentTime = refTime
while(True):
    #inputstring = input()

    # if inputstring != '':
    #     try:
    #         speed = int(inputstring)
    #     except:
    #         print('input value not an interger')
    # else:
    #     print( leftMotor.speed, rightMotor.speed)
    

    colorIntens = colorSensorCenter.reflected_light_intensity
    print(colorIntens)

    rightWeight = 100-colorIntens
    leftWeight =  colorIntens

    rightMotor.duty_cycle_sp = -(20+20*(rightWeight/100))
    leftMotor.duty_cycle_sp = -(20+20*(leftWeight/100))

    if(crossDetected()==1)
        rightMotor.duty_cycle_sp=0
        leftMotor.duty_cycle_sp=0
        break

