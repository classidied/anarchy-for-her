'''
Full control of the tank
- up/down/left/right keys to control movement
- "_/-" key to decrease speed
- "+/=" key to increase speed
- enter/return to shoot (hopefully)

'''
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  

GPIO.setwarnings(False)

# creating motor objects for the left and right drivetrains

# right side motors
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 15 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

# left side motors
GPIO.setup(16, GPIO.OUT)  # Set GPIO pin 16 to output mode.
pwm = GPIO.PWM(16, 100)   # Initialize PWM on pwmPin 100Hz frequency

'''
using knowledge of ranges
- clockwise from 6-13 (speed decreasing)
- counterclockwise from 15-22 (speed increasing)
- 14 is neutral point



algo 


'''