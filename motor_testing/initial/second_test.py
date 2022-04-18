import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # setting up GPIO board

# init motor (the pulse-width modulation signal to the pin attached to the motor)
GPIO.setup(15, GPIO.OUT)
pwm = GPIO.PWM(15, 100) # output signal on pin 15 at a freq of 100Hz

pwm.start(0) # start at 0 pwm 

try: 
    print("Rotating clockwise")
    # Figuring out if there are differences between the pwm values for clockwise (5-13)
    for x in range(5, 14, 1):
        print("--pwm value:", x)
        pwm.ChangeDutyCycle(x)
        time.sleep(1.5)
    time.sleep(0.5) # break between each value

    print("Rotating counterclockwise")
    # same thing but counterclockwise
    for y in range(15, 23, 1):
        print("--pwm value:", y)
        pwm.ChangeDutyCycle(y)
        time.sleep(1.5)
    time.sleep(0.5)
except KeyboardInterrupt:
    print("Program terminated")

# closing 
pwm.stop()
GPIO.cleanup()

'''
notes:
- pwm doesn't actually start at 5 it starts at 6
- consistent good speed from 6-10
- slow clockwise from 11-12 really slow at 13
- final range is from 6-13, speed decreasing as pwm increases

- extremely slow counterclockwise at 15
- slow counterclockwise at 16 (like speed of 13 pwm) 
- noticeable increasing speed from 15-19 
- 19-22 consistent good speed
- stops at 23
- final range is from 15 to 22, speed increases as pwm increases
'''