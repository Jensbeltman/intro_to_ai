print('hello')
from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from linefollower import LineFollower

rightMotor = LargeMotor(OUTPUT_A)
leftMotor = LargeMotor(OUTPUT_D)
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
colSFollower = ColorSensor(INPUT_2)
colSCrossDetection = ColorSensor(INPUT_2)

stopButton = TouchSensor(INPUT_1)
print(type(rightMotor),type(colorSensorCenter))

lineFollower = LineFollower(rightMotor, leftMotor,0.25,0,2)

crossDetected = False
turning = False
pushing = False

if __name__ == "__main_":
    while True:
        now = time.time()            # get the time
        
        colorIntens = colorSensorCenter.reflected_light_intensity
        lineFollower.follow(colorIntens)

        if stopButton.is_pressed(): 
            break

        elapsed = time.time() - now  # how long was it running?
        time.sleep(0.1-elapsed)       # sleep accordingly so the full iteration takes 1 second
        


        

        