print('Initializing')
from time import sleep, time
from crossDetection import crossDetection
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, LargeMotor, SpeedRPM
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.wheel import EV3Tire
from params import *
from planner import Plan
from robot import Robot


# Loading motor and sensor objects
# MoveDifferential(left_motor_port, right_motor_port, wheel_class, wheel_distance_mm)
leftMotor = LargeMotor(OUTPUT_B)
rightMotor = LargeMotor(OUTPUT_A)
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT

colSFollower = ColorSensor(INPUT_1)
colSCrossDetect = ColorSensor(INPUT_2)
stopButton = TouchSensor(INPUT_3)

robot = Robot(leftMotor,rightMotor,colSFollower,colSCrossDetect,baseSpeed)

# Initializing variables and behavior objects
state = lineFollowing
plan = Plan(planstring)
plan.nextStep
print('Initializing finished')
while True:
    # get the time
    # now = time()    
    # Handle stop button


    #robot.stop()
    #break

    ##### !!!!!------ START  --- TEST canPush ----------!!!!!
    #robot.readColS()
    robot.canPushed()
    break
    ##### !!!!!------ END  --- TEST canPush ----------!!!!!

    if stopButton.is_pressed:
        stopButton.wait_for_released()
        robot.stop()
        stopButton.wait_for_pressed()
        stopButton.wait_for_released()
    else:
        #Read inputs here
   
        #Cross detection
        robot.readColS()
        # !!!!!!!------ The crossDetection is changed! --- Have added robot. in front------!!!!!!
        if robot.crossDetection(robot.IcolSFollower,robot.IcolSCrossDetect,intersectionDetectThreshold):
            print('crossDetection')
            if plan.nextStep():
                print("Next step is :"+str(plan.action))
                if plan.action == 'l':
                    state = turnLeft
                if plan.action == 'r':
                    state = turnRight
                if plan.action == 'f':
                    robot.runStraight(baseSpeed)
                    robot.waitForRotation(0.15)
                    state = lineFollowing
                if plan.action == 'b':
                    state = uTurn
            else:
                robot.stop()
                print("plan done press stop button to reset")
                stopButton.wait_for_pressed()
                stopButton.wait_for_released()
                from params import *
                state = lineFollowing
                plan = Plan(planstring)


        #Line following
        if state == lineFollowing:
            robot.follow()
        elif state == uTurn:
            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.75)
            robot.rotateRight(baseSpeed*1.5)
            sleep(0.5)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=False,brake=False)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=True,brake=False)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=False,brake=False)
            
            robot.rotateLeft(baseSpeed/2)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=False,brake=False)

            robot.follow()
            state = lineFollowing
    

        #Turning
        elif state == turnLeft:
            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.4,brake=False)
            robot.rotateLeft(baseSpeed)
            robot.waitForColValue(robot.colSCrossDetect,lineDetectThreshold,ge=True,brake=False)
            robot.waitForColValue(robot.colSCrossDetect,lineDetectThreshold,ge=False,brake=True)
            robot.readColS()
            state=lineFollowing

        elif state == turnRight:
            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.4,brake=False)
            robot.rotateRight(baseSpeed)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=True,brake=False)
            robot.waitForColValue(robot.colSFollower,lineDetectThreshold,ge=False,brake=True)
            robot.readColS()
            state=lineFollowing

        elif state == canPush:
            pass



    
        # # manage timing 
        # elapsed = time() - now # calculating time elapsed for current loop
        # # if elapsed>dt:
        # # print(str(elapsed)+" seconds elapsed")
        # sleep(max([0,dt-elapsed])) # sleep accordingly so the full iteration takes 1 second