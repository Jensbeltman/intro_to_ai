

#from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import  INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from robot import *
from crossDetection import *
#from linefollower import LineFollower


#R = Right
#L = Left
#F = Forward
#B = Backwards

#RobNosePoint = is the where the front of the robot is pointing respect to the global view. - Where N(North) is up and W(West) is to the left
#N = North
#W = West
#E = East
#S = South 


#RobNosePoint <-This is the start condition - assumed that the robot will point up at the begining - can be changed in the future



# Steps:
# 1. Run to it see cross detection
# 2. Reset pos
# 3. Run x amount backwards
# 4. Reset pos
# 5. Turn 180deg
# 6. Reset pos
# 7. Run straight to it sees a cross detection 

# !!!Extra!!!! Implement that the local orientation change with 180deg!!!!!



def CanPushed():

    # Step 1
    while !(crossDetection(robot.IcolSFollower,robot.IcolSCrossDetect,intersectionDetectThreshold)):
        robot.runStraight(50)

    # Step 2
    robot.resetPosition()

    # Step 3
    while Pos_3 < 50:
        Pos_3 = robot.gePosition()
        robot.runStraight(-50) 

    # Step 4
    robot.resetPosition()    

    # Step 5
    while Pos_5 <180:
        Pos_5 = robot.gePosition()
        robot.rotateLeft(50)

    robot.resetPosition()

    # Step 7
    while !(crossDetection(robot.IcolSFollower,robot.IcolSCrossDetect,intersectionDetectThreshold)):
        robot.runStraight(50)

    




    # When the letter is capital then it's e.g. R=r+push(turn right and push the can to the next intersection) implementation -> rf (right,forward) - When it turns it on the can position!!!
    # Run x amount of distance back
    # Turn 180deg, or turn until it see black(line)
    # Drive forward to next intersection - Function end here at 





    



#Test program below

RobNosePoint='S'
arr=['N','N','E','N']

if __name__ == "__main__":

    

    



