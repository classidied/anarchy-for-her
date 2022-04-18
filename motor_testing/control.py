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

# if "up" key is pressed, return True
def move(key):
    fwd = Key.up
    if key == fwd:
        return True
    return False

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

try:
    print("Starting script...")
    while move(key) == True:
        # 
        
        print("hehe")
except KeyboardInterrupt:
    print("Goodbye!")

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
'''
# down key -> counter clockwise
        # right key -> increase speed clockwise
        # left key -> decrease speed clockwise
        # decrease speed
        print("Speed decreased to: ")
        # increase speed
        print("Speed increased to: ")
'''

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
