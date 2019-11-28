
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

if __name__ == "__main__":

    for x in arr:
        y=GlobalCoordinatesToLocal(x)
        print("The robot point dir= %s   |   Array input=%s   |   The output = %s" % (RobNosePoint,x,y))

    




