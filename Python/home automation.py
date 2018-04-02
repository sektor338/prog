import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

GPIO.setmode(GPIO.BCM)

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 18
lcd_d4 = 21
lcd_d5 = 20
lcd_d6 = 16
lcd_d7 = 12
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # piros gomb
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # sárga gomb
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # kék gomb
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pollák
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # geekbox

GPIO.setup(5, GPIO.OUT) #piros
GPIO.setup(6, GPIO.OUT) #sárga
GPIO.setup(13, GPIO.OUT) #zöld
GPIO.setup(19, GPIO.OUT) #kék

s = 4
t = 0.03

try:
    while True:
         button_state = GPIO.input(17)# piros gomb
         if button_state == False:
             GPIO.output(5, True)
             lcd.message('A konyhaban\neg a villany!')
             time.sleep(s)
             lcd.clear()
         else:
             GPIO.output(5, False)

         button_state = GPIO.input(27)# sárga gomb
         if button_state == False:
             GPIO.output(6, True)
             lcd.message('Az eloszobaban\neg a villany!')
             time.sleep(s)
             lcd.clear()
         else:
             GPIO.output(6, False)
        
         button_state = GPIO.input(22)# zöld gomb
         if button_state == False:
             GPIO.output(13, True)
             lcd.message('A furdoben\neg a villany!')
             time.sleep(s)
             lcd.clear()
         else:
             GPIO.output(13, False)

         button_state = GPIO.input(23) # kék gomb
         if button_state == False:
             GPIO.output(19, True)
             lcd.message('A garazsban\neg a villany!')
             time.sleep(s)
             lcd.clear()
         else:
             GPIO.output(19, False)

         button_state = GPIO.input(24)#pollak
         if button_state == False:
             for x in range(1):
                    for x in range(10):
                        GPIO.output(5, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(5, GPIO.LOW)
                        time.sleep(t)
                        GPIO.output(6, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(6, GPIO.LOW)
                        time.sleep(t)
                        GPIO.output(13, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(13, GPIO.LOW)
                        time.sleep(t)
                        GPIO.output(19, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(19, GPIO.LOW)
                        time.sleep(t)
                        GPIO.output(13, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(13, GPIO.LOW)
                        time.sleep(t)
                        GPIO.output(6, GPIO.HIGH)
                        time.sleep(t)
                        GPIO.output(6, GPIO.LOW)
                        time.sleep(t)
             lcd.message('Gyere a Pollakba\nes programozz!')
             time.sleep(s)
             lcd.clear()     

except:
    GPIO.cleanup()
