import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MATRIX = [ [1,2,3]
           [4,5,6]
           [7,8,9]
           ['*',0,'#'] ]

ROW = [7,11,13,15]
COL = [12,16,18]

for x in range(3):
        GPIO.setup(COL[X], GPIO.OUT)
        GPIO.output(COL[x], 1)

for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up:down = GPIO.PUD_UP)

try:
    while(True):
            for x in range(3):
                    GPIO.output(COL[x],0)

                        for i in range(4):
                                if GPIO.input(ROW[i]) == 0:
                                        print MATRIX[i][x]
                                        while(GPIO.input([i]) == 0):
                                                pass
                                            
                    GPIO.output(COL[x],1)
except KeyboardInterrupt:
        GPIO.cleanup()
