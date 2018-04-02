import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)#piros
GPIO.setup(16, GPIO.OUT)#sárga
GPIO.setup(18, GPIO.OUT)#zöld

for x in range(10):
	GPIO.output(12, GPIO.HIGH)
	print("Felkészülni!")
	time.sleep(0.15)
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.15)
	GPIO.output(16, GPIO.HIGH)
	print("Vigyázz!")
	time.sleep(0.15)
	GPIO.output(16, GPIO.LOW)
	time.sleep(0.15)
	GPIO.output(18, GPIO.HIGH)
	print("Rajt!!")
	time.sleep(0.15)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.15)
    
