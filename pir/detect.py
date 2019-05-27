import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

if __name__ == '__main__':
    while True:
        input = GPIO.input(18)
        if input==1:
            print("motion detected")
            time.sleep(1)
        else:
            print("no motion")
            time.sleep(1)
