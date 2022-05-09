# testing for up/down movement by pressing keys
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library
import keyboard

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins

GPIO.setwarnings(False)

# setting up motor input
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 15 to output mode.
pwm = GPIO.PWM(15, 100)   # Initialize PWM on pwmPin 100Hz frequency

# initializing pwm at 0
pwm.start(0)
    
try:
    while True:
        if keyboard.is_pressed('w'):
            print("Spinning clockwise...")
            # actually move the motor
            pwm.ChangeDutyCycle(6)
            time.sleep(2)
except KeyboardInterrupt:
    print("Terminating script")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
