# testing for up/down movement by pressing keys
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library
from pynput.keyboard import Key, Listener # to monitor key presses

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins

GPIO.setwarnings(False)

# setting up motor input
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 15 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

# initializing pwm at 0
pwm.start(0)

# '^[[A' is the bash char for the up key
# '^[[B' for down
# '^[[C' for right
# '^[[D' for left 

def move(key):
    # checking if the up key was pressed
    if key == Key.up:
        print("Spinning clockwise...")
    # actually move the motor
    pwm.ChangeDutyCycle(6)
    time.sleep()
    
    # stop moving if delete is pressed 
    if key == Key.delete: 
        pwm.ChangeDutyCycle(0)
        return False

# Collect all event until released
with Listener(on_press = move) as listener:
    listener.join()

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
