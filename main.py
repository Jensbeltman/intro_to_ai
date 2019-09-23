print('hello')
from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor 
import linefollower



rightMotor = LargeMotor(OUTPUT_A)
leftMotor = LargeMotor(OUTPUT_D)
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
colorSensorCenter = ColorSensor(INPUT_2)
print(type(rightMotor),type(colorSensorCenter))


print('its me..')


refTime = time()
currentTime = refTime
runTime = 10

print(currentTime-refTime)
while(runTime>(currentTime-refTime)):
    colorIntens = colorSensorCenter.reflected_light_intensity

    linefollower.follow(colorIntens, rightMotor, leftMotor)
    #inputstring = input()

    # if inputstring != '':
    #     try:
    #         speed = int(inputstring)
    #     except:
    #         print('input value not an interger')
    # else:
    #     print( leftMotor.speed, rightMotor.speed)
    

    currentTime=time()

rightMotor.duty_cycle_sp = 0
leftMotor.duty_cycle_sp = 0


    


    

    