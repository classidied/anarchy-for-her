# from https://www.explainingcomputers.com/pi_servos_video.html

# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(15,GPIO.OUT)
servo1 = GPIO.PWM(15, 100) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #Ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 & 180: '))
        servo1.ChangeDutyCycle(2+(angle/18)) # 7 corresponds to 90
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")


