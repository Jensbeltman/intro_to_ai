def follow(colorIntens, rightMotor, leftMotor):
    rightWeight = 100-colorIntens
    leftWeight =  colorIntens

    rightMotor.duty_cycle_sp = -(20+20*(rightWeight/100))
    leftMotor.duty_cycle_sp = -(20+20*(leftWeight/100))
    

