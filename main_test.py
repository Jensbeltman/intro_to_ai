print('Initializing')
from time import sleep, time
from crossDetection import crossDetection
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, SpeedPercent, LargeMotor, SpeedRPM
from ev3dev2.sensor import  INPUT_4, INPUT_2, INPUT_3
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

colSFollower = ColorSensor(INPUT_4)
colSCrossDetect = ColorSensor(INPUT_2)
stopButton = TouchSensor(INPUT_3)

robot = Robot(leftMotor,rightMotor,colSFollower,colSCrossDetect,baseSpeed)

# Initializing variables and behavior objects
state = lineFollowing
plan = Plan(planstring)
plan.nextStep

t = 0.0
tp = 0.0


print('Initializing finished')
while True:

    if stopButton.is_pressed:
        stopButton.wait_for_released(timeout_ms=3000)
        if not stopButton.is_released:
            stopButton.wait_for_released()
            robot.stop()
            print("The time took:")
            print(time()-t)
            print("plan reset press stop button to reset")
            stopButton.wait_for_pressed()
            stopButton.wait_for_released()
            
            
            state = lineFollowing
            plan = Plan(planstring)

        else:
            robot.stop()
            print("The time took:")
            print(time()-t)
            stopButton.wait_for_pressed()
            stopButton.wait_for_released()
            
            
    else:
        #Read inputs here
   
        #Cross detection
        
        # !!!!!!!------ The crossDetection is changed! --- Have added robot. in front------!!!!!!
        if robot.crossDetection() or state == idle:       
            robot.follow()  
            if plan.action != None:
                duration = time()-t
                robot.timeSaveArray.append(duration)
            t=time()
            #print('crossDetection')
            if plan.nextStep():
                
                    
                
               # print("Next step is :"+str(plan.action))
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
                if plan.action == 'p':
                    state = canPush
                
            else:
                duration = t-tp
                robot.timeSaveArray.append(duration)
                robot.stop()          
                print("plan done press stop button to reset")

                for i in range (len(robot.timeSaveArray)):
                    print(robot.timeSaveArray[i],sep="\n")
                robot.timeSaveArray=[]
                stopButton.wait_for_pressed()
                stopButton.wait_for_released()
                
                from params import *
                state = lineFollowing
                plan = Plan(planstring)
                
                


        #Line following
        if state == lineFollowing:
            robot.follow()
        elif state == uTurn:
            t=time()
            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.5,brake=False)
            robot.rotateRight(baseSpeed/2)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.8,ge=True,brake=False)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.6,ge=False,brake=False)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.8,ge=True,brake=False)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.6,ge=False,brake=True)
            robot.readColS()
            
            robot.timeSaveArray.append(time()-t)

            state=lineFollowing
    

        #Turning
        elif state == turnLeft:
            t=time()

            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.5,brake=False)
            robot.rotateLeft(baseSpeed)
            robot.waitForRotation(0.35,brake=False)
            robot.rotateLeft(baseSpeed/2)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.6,ge=False,brake=False)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.8,ge=True,brake=False)
            robot.rotateRight(baseSpeed/3)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.4,ge=False,brake=True)
            
            robot.timeSaveArray.append(time()-t)
            robot.readColS()          
            state=lineFollowing

        elif state == turnRight:
            t=time()

            robot.runStraight(baseSpeed)
            robot.waitForRotation(0.55,brake=False)
            robot.rotateRight(baseSpeed)
            robot.waitForRotation(0.35,brake=False)
            robot.rotateRight(baseSpeed/2)
            robot.waitForColValue(robot.colSFollower,robot.threshold*0.6,ge=False,brake=True)
            robot.readColS()
            robot.timeSaveArray.append(time()-t)
            state=lineFollowing

        elif state == canPush:
            t=time()
            robot.canPushed()
            robot.timeSaveArray.append(time()-t)
            state = idle
