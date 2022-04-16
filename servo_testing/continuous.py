#!/usr/bin/python
# import libraries
import RPi.GPIO as GPIO
import time

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)

# Set pin 13 as an output, setting servo2 as pin 13 pwm
GPIO.setup(13, GPIO.OUT)

# make servos
servo1 = GPIO.PWM(11, 50) # Note 11 is pin, 50 = 50Hz pulse -> change pulse to change the power?
servo2 = GPIO.PWM(13, 50)

servo1.start(0)
servo2.start(0)

try:
    while True:
        # first set the servo into place, at 0 degrees (duty cycle 2)
        servo1.ChangeDutyCycle(2)
        servo2.ChangeDutyCycle(2)
        time.sleep(1)
        # turn servo1 180 degrees, servo2 90 degrees
        servo1.ChangeDutyCycle(12)
        servo2.ChangeDutyCycle(7)
        time.sleep(1)
        print("hopefully turned 180 or 90")
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)
        # turn servo1 back to 0, servo2 to 180
        servo1.ChangeDutyCycle(2)
        servo2.ChangeDutyCycle(12)
        print("went back to 0")
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)
except KeyboardInterrupt:
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
    print("Goodbye!")

'''
Notes:
- use .ChangeDutyCycle(0) to stop the servo from jittering when it shouldn't be moving; this stops any signals from being sent
- if you want to actually make it continuously spin, put the power wire on a 3v3 instead of 5v 
and for some reason it'll work, the only issue is that the only way to stop it is to physically
disconnect it from power (removing pins/powering off the pi completely)

'''






