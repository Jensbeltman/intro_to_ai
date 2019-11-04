print('hello')
from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from linefollower import LineFollower

rightMotor = LargeMotor(OUTPUT_A)
leftMotor = LargeMotor(OUTPUT_D)
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
colSFollower = ColorSensor(INPUT_1)
colSCrossDetect = ColorSensor(INPUT_2)
stopButton = TouchSensor(INPUT_3)

stopButton = TouchSensor(INPUT_1)
print(type(rightMotor),type(colorSensorCenter))

lineFollower = LineFollower(rightMotor, leftMotor,0.25,0,2)

crossDetected = False
turning = False
pushing = False

if __name__ == "__main_":
    while True:
        now = time.time()            # get the time
        # Reading inputs
        if stopButton.is_pressed(): break
        icolSFollower = colSFollower.reflected_light_intensity
        icolSCrossDetect = colSCrossDetect.reflected_light_intensity
        #Cross detection
        crossDetected = crossDetection(icolSFollower,icolSCrossDetect,10)

        # Upcomming statemachine
        if crossDetected: break

        lineFollower.follow(colorIntens)

        elapsed = time.time() - now  # how long was it running?
        time.sleep(0.1-elapsed)       # sleep accordingly so the full iteration takes 1 second
        


        

        