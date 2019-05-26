import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer=23

GPIO.setup(buzzer,GPIO.OUT)

while True:
    print("Beep")
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(2)
    print("No beep")
    GPIO.output(buzzer,GPIO.LOW)
    sleep(2)
