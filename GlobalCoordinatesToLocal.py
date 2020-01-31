
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
# 
def GlobalCoordinatesToLocal(GlobalCoordinateInput):

    X = GlobalCoordinateInput
    global RobNosePoint

    if X == RobNosePoint:
        outputDirection='F'

    if X == 'N' and RobNosePoint == 'W':
        outputDirection ='R'
        RobNosePoint=X 
    elif X == 'N' and RobNosePoint == 'E':
        outputDirection ='L'  
        RobNosePoint=X     
    elif X == 'N' and RobNosePoint == 'S':
        outputDirection ='B'  # Need to driving backwards here - Save it as it's here and handle the output of the function later?
        RobNosePoint=X  # This needs to change but if the robot doesn't turn then it will drive backwards, and still keep the pointing direction. WHAT TO do here????  


    if X == 'W' and RobNosePoint == 'N':
        outputDirection ='L'
        RobNosePoint=X
    elif X == 'W' and RobNosePoint == 'S':
        outputDirection ='R'  
        RobNosePoint=X     
    elif X == 'W' and RobNosePoint == 'E':
        outputDirection ='B'  # Need to driving backwards here - Save it as it's here and handle the output of the function later?
        RobNosePoint=X  # This needs to change but if the robot doesn't turn then it will drive backwards, and still keep the pointing direction. WHAT TO do here????    

    if X == 'E' and RobNosePoint == 'S':
        outputDirection ='L'
        RobNosePoint=X
    elif X == 'E' and RobNosePoint == 'N':
        outputDirection ='R'  
        RobNosePoint=X     
    elif X == 'E' and RobNosePoint == 'W':
        outputDirection ='B'  # Need to driving backwards here - Save it as it's here and handle the output of the function later?
        RobNosePoint=X  # This needs to change but if the robot doesn't turn then it will drive backwards, and still keep the pointing direction. WHAT TO do here????  

    if X == 'S' and RobNosePoint == 'W':
        outputDirection ='L'
        RobNosePoint=X
    elif X == 'S' and RobNosePoint == 'E':
        outputDirection ='R'  
        RobNosePoint=X     
    elif X == 'S' and RobNosePoint == 'N':
        outputDirection ='B'  # Need to driving backwards here - Save it as it's here and handle the output of the function later?
        RobNosePoint=X  # This needs to change but if the robot doesn't turn then it will drive backwards, and still keep the pointing direction. WHAT TO do here????  
    
    return outputDirection 


#Test program below

RobNosePoint='S'
arr=['N','N','E','N']



def isUpperCase(c):
    return any([c == uc for uc in ['U','D','L','R']])

def toLowerCase(c):
    if isUpperCase(c):
        return chr(ord(c) + 32)

def isSameDirection(state):
    c1 = ord(state[0])
    c2 = ord(state[1])
    return (c1 == c2+32 or c2 == c1+32 or c1 == c2)

def isOppositeDirection(state):
    return any([state == oppositePair for oppositePair in [('u','d'),('d','u'),('l','r'),('r','l')]])



def getMove(state):
    # up global direction
    if state == ('u','l'):
        return 'l'
    elif state == ('u','r'):
        return 'r'
    # down global direction
    elif state == ('d','l'):
        return 'r'
    elif state == ('d','r'):
        return 'l'
    # left global direction
    elif state == ('l','u'):
        return 'r'
    elif state == ('l','d'):
        return 'l'
    # right global direction
    elif state == ('r','u'):
        return 'l'
    elif state == ('r','d'):
        return 'r'
    else:
        print(state)

 
competitionMap = 'llllUddlluRRRRRdrUUruulldRRdldlluLuulldRurDDullDRdRRRdrUUruurrdLulDulldRddlllluurDldRRRdrUUdlllldlluRRRRRdrU'
competitionMapOld = ''

def globalToLocal(globalMap):
    localMap =''
    globalD = 'u'

    for i in range(len(globalMap)):
        globalMove = globalMap[i]
        
        if i>0:
            globalD = globalMap[i-1]
            if isUpperCase(globalD):
                globalD = toLowerCase(globalD)
        


        state = (globalD,globalMove)

        if not isUpperCase(state[1]):
            if not isSameDirection(state):
                if not isOppositeDirection(state):
                    localMap+= getMove(state)
                else:
                    localMap+= 'b'
            else:
                localMap+= 'f'
        else:
            state = (state[0],toLowerCase(state[1]))
            if (i+1)<len(globalMap):
                if not isSameDirection(state):
                    if not isOppositeDirection(state):
                        localMap+= getMove(state)
                    else:
                        localMap+= 'b'
                else:
                    localMap+= 'f'

                nextMove = globalMap[i+1]
                if not toLowerCase(nextMove) == state[1]:
                    localMap+='p'
            else:
                if not isSameDirection(state):
                    if not isOppositeDirection(state):
                        localMap+= getMove(state)
                    else:
                        localMap+= 'b'
                else:
                    localMap+= 'f'
                localMap+='p'

    #print(globalMap)
    return localMap

if __name__ == "__main__":
    
    globalMap = 'llllUddlluRRRRRdrUUruulldRRdldlluLuulldRurDDullDRdRRRdrUUruurrdLulDulldRddlllluurDldRRRdrUUdlllldlluRRRRRdrU'
    print(globalToLocal(globalMap))


