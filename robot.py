from params import *
import math
#from crossDetection *

class Robot():
    def __init__(self,left_motor,right_motor,colSFollower,colSCrossDetect,dc):
        self.leftMotor = left_motor
        self.rightMotor = right_motor
        self.ductyCycle = dc
        self.colSFollower = colSFollower
        self.colSCrossDetect = colSCrossDetect
        self.IcolSFollower = colSFollower.reflected_light_intensity
        self.IcolSCrossDetect = colSCrossDetect.reflected_light_intensity
        # self.bufferFollower = [50 for i in range(avrWindow)]
        self.bufferCrossDetect = [iRange/4 for i in range(avrWindow)]
        self.bufferIdx = 0
        self.crossDetected = False
        self.threshold = iRange/4
        # Line following
        self.prevIDev = 0
        # For wheel
        self.Pos = 0


    def readColS(self):
        self.IcolSFollower = self.colSFollower.reflected_light_intensity
        self.IcolSCrossDetect = self.colSCrossDetect.reflected_light_intensity
        # self.bufferFollower[self.bufferIdx] = self.IcolSFollower 
        # self.bufferCrossDetect[self.bufferIdx] = self.IcolSCrossDetect 

        # self.bufferIdx = (self.bufferIdx+1)%10

        return (self.IcolSCrossDetect,self.IcolSFollower)

    def stop(self):
        self.rightMotor.duty_cycle_sp = 0
        self.leftMotor.duty_cycle_sp = 0   

    def follow(self):
        self.readColS()
        self.bufferCrossDetect[self.bufferIdx] = self.IcolSCrossDetect 
        self.bufferIdx = (self.bufferIdx+1)%avrWindow
        self.threshold = sum(self.bufferCrossDetect)/float(avrWindow)
        

        iDev = (iTarget-self.IcolSFollower)/(iRange/2)

        rightWeight = -iDev*P
        leftWeight =  iDev*P

        self.rightMotor.duty_cycle_sp = (self.ductyCycle+rightWeight*(100-self.ductyCycle))
        self.leftMotor.duty_cycle_sp = (self.ductyCycle+leftWeight*(100-self.ductyCycle))


    def waitForColValue(self, sensor, threshold,ge=True,brake=True):
        while True:
            if ge:
                if sensor.reflected_light_intensity > threshold:
                    break
            else:
                if sensor.reflected_light_intensity < threshold:
                    break           
        if brake:
            self.stop()

    def waitForRotation(self,rotations,brake=True):
        maxCount = self.leftMotor.count_per_rot*rotations
        self.resetPosition()
        while True:
            maxVal = max([abs(self.leftMotor.position), abs(self.rightMotor.position)])
            if maxCount <= maxVal:
                break
        if brake:
            self.stop()

    def resetBuffer(self):
        pass
        # self.bufferFollower = [50 for i in range(avrWindow)]
        # self.bufferCrossDetect = [50 for i in range(avrWindow)]

    def setDC(self,lDC,rDC):
        self.rightMotor.duty_cycle_sp = rDC
        self.leftMotor.duty_cycle_sp = lDC
        self.rightMotor.duty_cycle_sp = rDC
        self.leftMotor.duty_cycle_sp = lDC

    def rotateRight(self,dc):
        self.setDC(dc,-dc)

    def rotateLeft(self,dc):
        self.setDC(-dc,dc)
        

    def runStraight(self,DC):
        self.setDC(DC,DC)

    def resetPosition(self):
        self.leftMotor.position = 0
        self.rightMotor.position = 0

    def getPosition(self):
        return self.leftMotor.position

    def crossDetection(self):
        return (self.IcolSCrossDetect<=(0.8*self.threshold))


    def canPushed(self):

        crossValue = 0

        self.runStraight(baseSpeed)
        self.waitForRotation(0.15)
        # Step 1
        self.resetPosition()
        
        # Step 2
        self.Pos = self.getPosition()
        #print(self.Pos)

        while self.Pos < (lineLenght_WheelPos-180):
            #print(self.Pos)
            self.Pos = self.getPosition()    
            self.follow()
        '''
        print(crossValue)
        print(crossValue)
        print(crossValue)
        '''
        # Step 3
        #self.stop()
        


         # Step 5
        while True:
            self.runStraight(-50)
            self.readColS()    
            if self.crossDetection():
                self.stop()
                break


        # Step 4
        '''
        while self.Pos >= 0:
            
            self.Pos = self.getPosition()
            self.runStraight(-50)
            
            if self.Pos <= 0:
                self.stop()
                break
            
            self.readColS()
            if self.crossDetection():
                self.stop()
                break
        '''
    

        self.stop()


