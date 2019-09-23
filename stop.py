print('hello')
from time import sleep, time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent


rightMotor = LargeMotor(OUTPUT_A)
leftMotor = LargeMotor(OUTPUT_D)
rightMotor.command = rightMotor.COMMAND_RUN_DIRECT
leftMotor.command = leftMotor.COMMAND_RUN_DIRECT




    

rightMotor.duty_cycle_sp = 0
leftMotor.duty_cycle_sp = 0

    

    