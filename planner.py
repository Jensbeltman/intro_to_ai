class Plan():
    def __init__(self, plan="rr"):
        if len(plan)>0:        
            self.plan = plan
            self.prevAction = None
            self.stepIdx = 0
            self.planLength = len(plan)
            self.action = None
        else:
            print("Plan initialization failed")

    def isLastAction(self):
        return stepIdx == self.planLength-1

    def nextStep(self):
        if self.action == None:
            self.stepIdx=0
            self.action = self.plan[self.stepIdx]
            return True
        elif self.stepIdx+1 < self.planLength:
            self.stepIdx+=1
            self.prevAction = self.action
            self.action = self.plan[self.stepIdx]
            return True 
        else:
            self.reset()
            return False
    def reset(self):
            self.prevAction = None
            self.stepIdx = 0
            self.action = None


    