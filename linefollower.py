import time

class LineFollower():
    def __init__(self,rightMotor, leftMotor,P=1,I=0,D=0):
        self.iMM = [0, 100]
        self.iRange = 100
        self.iTarget = 100/2
        self.P = P
        self.I = I
        self.D = D
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor
        self.prevIDev = 0
        self.prevTime = 1000000
        
    
    def follow(self,colorIntens):
        iDev = (self.iTarget-colorIntens)/self.iRange
        currentTime = time.time()*1000
        iDevD= (self.prevIDev-iDev)/((currentTime-self.prevTime))
        self.prevIDev = iDevD
        self.prevTime = currentTime

        rightWeight = iDev*self.P+iDevD*self.D
        leftWeight =  -(iDev*self.P+iDevD*self.D)

        self.rightMotor.duty_cycle_sp = -(50+rightWeight*100)
        self.leftMotor.duty_cycle_sp = -(50+leftWeight*100)
        

