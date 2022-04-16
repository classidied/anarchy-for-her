# get input, spin for x seconds in n direction (clockwise/counterclockwise)

import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins

GPIO.setwarnings(False)

# motor 1
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 15 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

# initializing pwm at 0
pwm.start(0)
'''
using knowledge of ranges
- clockwise from 6-13 (speed decreasing)
- counterclockwise from 15-22 (speed increasing)
- 14 is neutral point
'''

try:
    while True:
        # take user input for direction, seconds
        direction = int(input("Which way to spin? (clockwise: 1, counterclockwise: 2):\n"))
        seconds = int(input("For how many seconds?\n"))
        # spin clockwise
        if direction == 1:
            print("Spinning clockwise for ", seconds, " seconds:")
            pwm.ChangeDutyCycle(11)
            time.sleep(seconds)
            pwm.ChangeDutyCycle(0) # stop signal
        # spin counterclockwise 
        elif direction == 2: 
            print("Spinning counterclockwise for ", seconds, "seconds")
            pwm.ChangeDutyCycle(15)
            time.sleep(seconds)
            pwm.ChangeDutyCycle(0)
        else:
            print("invalid direction input")
            quit()
except KeyboardInterrupt:
    print("Goodbye!")


pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
