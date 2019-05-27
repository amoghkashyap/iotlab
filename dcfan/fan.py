import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

fan=23

GPIO.setup(fan,GPIO.OUT)

while True:
    print("on")
    GPIO.output(fan,GPIO.HIGH)
    sleep(5)
    print("off")
    GPIO.output(fan,GPIO.LOW)
    sleep(2)
