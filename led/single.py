import RPi.GPIO as GPIO
import time

led = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

def ledTrigger():
    print ("LED on")
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)

if __name__ == "__main__":
    while True:
        ledTrigger()

