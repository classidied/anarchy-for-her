import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

# indicating which pin to send signals to 
GPIO.setup(15, GPIO.OUT)
pwm = GPIO.PWM(15,100)

pwm.start(0)

try:
    pwm.ChangeDutyCycle(11)
    time.sleep(3)
except KeyboardInterrupt:
    print("End")

pwm.stop()
GPIO.cleanup()