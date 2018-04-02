import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP) # piros gomb akkor ne
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP) # sárga gomb okos vagy
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb ja oké
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # kék gomb pollák
GPIO.setup(12, GPIO.OUT)  # piros led
GPIO.setup(16, GPIO.OUT)  # sárga led
GPIO.setup(18, GPIO.OUT)  # zöld led
GPIO.setup(22, GPIO.OUT)  # kék led

GPIO.setwarnings(False)

uname = input("Hello mi a neve?")

print("Üdv", uname + ".", )

print("Akarsz válaszolni egy kérdésre? Ha igen nyomd meg a zöld gombot. Ha nem akkor nyomd meg a piros gombot.")

try:
    while True:
         button_state = GPIO.input(32)
         if button_state == False:
             GPIO.output(12, True)
             print("Akkor ne!")
             time.sleep(0.5)
         else:
             GPIO.output(12, False)

         button_state = GPIO.input(36)
         if button_state == False:
             GPIO.output(16, True)
             print("Okos vagy?")
             time.sleep(0.5)
         else:
             GPIO.output(16, False)
         button_state = GPIO.input(38)
         if button_state == False:
             GPIO.output(18, True)
             print("Ja, oké")
             time.sleep(0.5)
         else:
             GPIO.output(18, False)

         button_state = GPIO.input(40)
         if button_state == False:
             GPIO.output(22, True)
             print("Gyere a Pollákba infósnak vagy elketrósnak!")
             time.sleep(0.5)
         else:
             GPIO.output(22, False)
except:
    GPIO.cleanup()


