#  MBTechWorks.com 2016 https://www.mbtechworks.com/projects/raspberry-pi-pwm.html
#  Pulse Width Modulation (PWM) demo to cycle brightness of an LED

import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

# set warnings to false
GPIO.setwarnings(False)

GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle

try:
  while True:                      # Loop until Ctl C is pressed to stop.
    for dc in range(0, 100, 10):    # Loop 0 to 100 stepping dc by 5 each loop
      pwm.ChangeDutyCycle(dc)
      time.sleep(1)             # wait .05 seconds at current LED brightness
      print(dc)
    for dc in range(100, 0, -10):    # Loop 95 to 5 stepping dc down by 5 each loop
      pwm.ChangeDutyCycle(dc)
      time.sleep(2)             # wait .05 seconds at current LED brightness
      print(dc)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
'''
this is giving me cancer maybe I'm just dumb 

runs clockwise for 1s (prints 0, 10) and then runs counter clockwise for 1s (prints 20)
then does nothing until it reaches 20, 10, or 0 again
'''