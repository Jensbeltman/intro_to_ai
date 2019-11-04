

def crossDetection(colorIntensCenter,colorIntensRight,lightValue = 10):

    if((colorIntensRight<=lightValue) and (colorIntensCenter<=lightValue)):
        retrunValue=True
    else:
        retrunValue=False

    return retrunValue
