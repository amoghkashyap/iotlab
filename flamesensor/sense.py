import RPi.GPIO as GPIO
from time import sleep

channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel,GPIO.IN)


while True:
    input = GPIO.input(channel)
    if input==1:
        print("flame detected")
        sleep(1)
    else:
        print("No flame detected")
        sleep(1)
