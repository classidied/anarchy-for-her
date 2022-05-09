# import libraries
import RPi.GPIO as GPIO
import time

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# pin 11 will be used to send signals/pwm
GPIO.setup(11,GPIO.OUT)

# creating servo object
servo1 = GPIO.PWM(11, 50)

try:
    print("Receiving input...")
    # if raw_input exists????
except KeyboardInterrupt:
    print("Goodbye!")
