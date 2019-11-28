

#from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from robot import Robot
from crossDetection import crossDetection
from params import *
#from linefollower import LineFollower



# Steps:
# 1. Reset pos
# 2. Run x amount forward
# 3. Stop rob
# 4. Run backwards so x gives 0 in pos  
#  exclude this maybe if 4 doesn't work             ---- . Run straight to it sees a cross detection 

# !!!Extra!!!! Implement that the local orientation change with 180deg!!!!!






def canPushed(rob):

    crossValue = 0

    rob.runStraight(baseSpeed)
    rob.waitForRotation(0.15)
    # Step 1
    rob.resetPosition()
    
    # Step 2
    Pos_3 = rob.getPosition()
    print(Pos_3)
    while Pos_3 < (lineLenght_WheelPos-100):
        print(Pos_3)
        Pos_3 = rob.getPosition()    
        rob.follow()
        rob.readColS()
        if crossDetection(rob.IcolSFollower,rob.IcolSCrossDetect,intersectionDetectThreshold):
            crossValue = rob.getPosition()
            break

    print(crossValue)
    print(crossValue)
    print(crossValue)
    # Step 3
    #rob.stop()
    


 # Step 5
    while True:
        rob.runStraight(-50)
        rob.readColS()
       if crossDetection(rob.IcolSFollower,rob.IcolSCrossDetect,intersectionDetectThreshold):
           rob.stop()
           break


    # Step 4
    while Pos_3 >= 0:
        
        Pos_3 = rob.getPosition()
        rob.runStraight(-50)
        '''
        if Pos_3 <= 0:
            rob.stop()
            break
        '''
        rob.readColS()
        if crossDetection(rob.IcolSFollower,rob.IcolSCrossDetect,intersectionDetectThreshold):
           rob.stop()
           break

   

    rob.stop()


     

    

    



