import RPi.GPIO as GPIO  # import GPIO library
from RpiMotorLib import RpiMotorLib  # import mdotor library
import time  # import time library

direction = 22
step = 23
EN_pin = 24

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21, 21, 21), "A4988")
GPIO.setup(EN_pin, GPIO.OUT)  # set enable pin as output

###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin, GPIO.LOW)  # pull enable to low to enable motor
# call the function, pass the arguments
mymotortest.motor_go(False, "Full" , 100, .01, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
