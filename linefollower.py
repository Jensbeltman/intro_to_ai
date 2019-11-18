import time
from params import *
import math

class LineFollower():
    def __init__(self,mDiff):
        self.mDiff = mDiff
        self.prevIDev = 0

    def follow(self,colorIntens):
        iDev = (iTarget-colorIntens)/(iRange/2)
        iDevD= (self.prevIDev-iDev)/dt
        self.prevIDev = iDevD

        rightWeight = -iDev*P
        leftWeight =  iDev*P
        
        if math.isfinite(rightWeight) and math.isfinite(leftWeight) :
            self.mDiff.right_motor.duty_cycle_sp = (baseSpeed+rightWeight*(100-baseSpeed))
            self.mDiff.left_motor.duty_cycle_sp = (baseSpeed+leftWeight*(100-baseSpeed))
        else:
            print("Dev not finite")
    
