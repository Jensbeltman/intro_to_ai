#Gloabal
distBettwenWheels = 90#mm
baseSpeed = 60
iTarget=32
iRange=64
#planstring="rrrrrrrrrrrrbllllllllllllbrrrrrrrrrrrrbllllllllllll" # For testing the turning
planstring="lfffrpbfrfrrffffprllfprlflfllfprrlrfrlprflfllplrrfpblflplprlffprllfprlfrfrrprllpblfllprfrfffrfrrprllffprllfpbrffflrfrrffffprllp"

#States
lineFollowing = 1
turnRight = 2
turnLeft = 3
canPush = 4
continueForward = 5
uTurn = 6
idle = 10

#Linefollowing
P = 0.3
I = 0.0
D = 0.0
dt = 0.05

#Crossdetection

lineUpper = iTarget
lineLower = iTarget-(iRange/4)
#lineLower = 12
lineMiddle = iTarget-(iRange/4)
continueDist = 15
whiteThreshold = 50
avrWindow = 20

#Turning
turnSpeed = 30
turnDeg = 90
turnRightDist = 90
turnLeftDist = 95
sleepTime = 1.0
pos = 0

lineLenght_WheelPos=567