#Gloabal
distBettwenWheels = 90#mm
baseSpeed = 60
iTarget=33
iRange=56
planstring="ffrllllfrrflu"

#States
lineFollowing = 1
turnRight = 2
turnLeft = 3
pushing = 4
continueForward = 5
uTurn = 6
idle = 10

#Linefollowing
P = 0.3
I = 0.0
D = 0.0
dt = 0.05

#Crossdetection
intersectionDetectThreshold = 35
lineDetectThreshold = 25
continueDist = 15
whiteThreshold = 50

#Turning
turnSpeed = 30
turnDeg = 90
turnRightDist = 90
turnLeftDist = 95
sleepTime = 1.0
pos = 0

