import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
for i in range(10):
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(16,GPIO.HIGH)
