import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

# motor 1
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 15 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

pwm.start(0)

try:
  print("rotating counterclockwise:")
  for dc in range(100, 0, -1):    
    pwm.ChangeDutyCycle(dc)
    time.sleep(5)             
    print(dc)
except KeyboardInterrupt:
  print("Program terminated")

pwm.stop()                         
GPIO.cleanup()                     # resets GPIO ports used back to input mode

'''
with clockwise.py (noting the dc values)
- started rotating clockwise at 5, slowed/stopped at 13
- started rotating counter clockwise at 15, slowed/stopped at 22
- stopped entirely at 22 
'''
