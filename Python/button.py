import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) # piros gomb
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb
GPIO.setup(12, GPIO.OUT)  # piros led
GPIO.setup(18, GPIO.OUT)  # z�ld led

try:
    while True:
         button_state = GPIO.input(38)
         if button_state == False:
             GPIO.output(12, True)
             print('Válaszd a Pollákot!')
             time.sleep(0.5)

         button_state = GPIO.input(40)
         if button_state == False:
             GPIO.output(12, False)
             print('Válaszd a Pollákot!')
             time.sleep(0.5)

except:
    GPIO.cleanup()
