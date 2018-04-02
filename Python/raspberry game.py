import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) #enter
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) #buttoni
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) #buttonn
GPIO.setup(18,GPIO.OUT) #ledi
GPIO.setup(18,GPIO.OUT) #ledn

MATRIX = [ [1,2,3]
           [4,5,6]
           [7,8,9]
           ['*',0,'#'] ]

ROW = [7,11,13,15]
COL = [12,16,18,22] #csak 3 kell

for x in range(4):
        GPIO.setup(COL[X], GPIO.OUT)
        GPIO.output(COL[x], 1)

for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up:down = GPIO.PUD_UP)

try:
    while(True):
            for x in range(4):
                    GPIO.output(COL[x],0)

                        for i in range(4):
                                if GPIO.input(ROW[i]) == 0:
                                        print MATRIX[i][x]
                                        while(GPIO.input([i]) == 0):
                                                pass
                                            
                    GPIO.output(COL[x],1)
except KeyboardInterrupt:
        GPIO.cleanup()


number = random.randint(1, 10)
tries = 1

uname = input("Hello mi a neve?")

print("Üdv", uname + ".", )

question = input("Akarsz játszani? [(GPIO.input(23) ==1)/(GPIO.input(24) ==1)]")
if question == "(GPIO.input(24) == 1)":
    print("Soros-e vagy?")

if question == "(GPIO.input(23) == 1)":
    print("Gondoltam egy számra 1 és 10 között")
    guess = int(input("Találgass: "))
    if guess > number:
        print("Kisebb számra gondoltam")
    if guess < number:
        print("Nagyobb számra gondoltam")
    while guess != number:
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        tries += 1
        guess = int(input("Próbáld újra"))
    if guess == number:
        print("Eltaláltad! Te nyertél! A szám a", number,\
                "volt és ", tries, "próbálkozással sikerült kitalálni!")
    while true:
        if guess == number:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
