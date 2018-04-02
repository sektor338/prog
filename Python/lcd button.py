#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(5, GPIO.OUT)
             
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

try:
    while True:
         button_state = GPIO.input(24)
         if button_state == False:
            lcd.message(" Valaszd te is\n  a Pollakot!")
            GPIO.output(5, True)
            time.sleep(1)
            lcd.clear()
         else:
             GPIO.output(5, False)
             
except:
    GPIO.cleanup()
