print('Initializing')
from time import sleep, time
from crossDetection import crossDetection
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, MoveDifferential, SpeedRPM
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.wheel import EV3Tire
from linefollower import LineFollower
from params import *
from planner import Plan

# Loading motor and sensor objects
mDiff = MoveDifferential(OUTPUT_B, OUTPUT_A, EV3Tire, distBettwenWheels)
mDiff.run_direct()
colSFollower = ColorSensor(INPUT_1)
colSCrossDetect = ColorSensor(INPUT_2)
stopButton = TouchSensor(INPUT_3)

# Initializing variables and behavior objects
state = lineFollowing
lineFollower = LineFollower(mDiff=mDiff)

plan = Plan(planstring)
plan.nextStep
print('Initializing finished press button to start')
while True:
    # get the time
    # now = time()    
    # Handle stop button
    if stopButton.is_pressed:
        stopButton.wait_for_released()
        mDiff.reset()
        stopButton.wait_for_pressed()
        mDiff.run_direct()
        stopButton.wait_for_released()
    else:
        #Read inputs here
        icolSFollower = colSFollower.reflected_light_intensity
        icolSCrossDetect = colSCrossDetect.reflected_light_intensity
        #Cross detection
        if crossDetection(icolSFollower,icolSCrossDetect,lineDetectThreshold):
            print('crossDetection')
            if plan.nextStep():
                print("Next step is :"+str(plan.action))
                if plan.action == 'l':
                    state = turnLeft
                if plan.action == 'r':
                    state = turnRight
                if plan.action == 's':
                    mDiff.on_for_distance(baseSpeed,continueDist,brake=False)
                    mDiff.run_direct()
                    state = lineFollowing
            else:
                mDiff.reset()
                print("plan done press stop button to reset")
                stopButton.wait_for_pressed()
                stopButton.wait_for_released()
                from params import *
                plan = Plan(planstring)


        #Line following
        if state == lineFollowing:
             lineFollower.follow(icolSFollower)

        #Turning
        elif state == turnLeft:
            mDiff.on_for_distance(turnSpeed,turnLeftDist,brake=False)
            mDiff.turn_left(turnSpeed,turnDeg,brake=False)
            mDiff.run_direct()
            state=lineFollowing
        elif state == turnRight:
            mDiff.on_for_distance(turnSpeed,turnRightDist,brake=False)
            mDiff.turn_right(turnSpeed,turnDeg,brake=False)
            mDiff.run_direct()
            state=lineFollowing



    
        # # manage timing 
        # elapsed = time() - now # calculating time elapsed for current loop
        # # if elapsed>dt:
        # # print(str(elapsed)+" seconds elapsed")
        # sleep(max([0,dt-elapsed])) # sleep accordingly so the full iteration takes 1 second