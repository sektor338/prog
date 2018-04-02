import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) # piros gomb
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb
GPIO.setup(12, GPIO.OUT)  # piros led
GPIO.setup(18, GPIO.OUT)  # zöld led

GPIO.setwarnings(False)

uname = input("Hello mi a neve?")

print("Üdv", uname + ".", )

print("Akarsz válaszolni egy kérdésre? Ha igen nyomd meg a zöld gombot, 40. Ha nem akkor nyomd meg a piros gombot, 16.")

try:
    while True:
         button_state = GPIO.input(38)
         if button_state == False:
             GPIO.output(12, True)
             print("Akkor ne!")
             time.sleep(0.5)
         else:
             GPIO.output(12, False)

         button_state = GPIO.input(40)
         if button_state == False:
             GPIO.output(18, True)
             print("Okos vagy?")
             time.sleep(0.5)
         else:
             GPIO.output(18, False)
except:
    GPIO.cleanup()

