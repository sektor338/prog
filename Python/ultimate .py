import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # piros gomb
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # zöld gomb

GPIO.setup(18, GPIO.OUT) #piros
GPIO.setup(23, GPIO.OUT) #sárga
GPIO.setup(24, GPIO.OUT) #zöld
GPIO.setup(25, GPIO.OUT) #kék

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=17

t = time.sleep(s)
s = 0.02

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(11, 17)

try:
    while True:
         button_state = GPIO.input(16)
         if button_state == False:
             GPIO.output(18, True)
             print('Válaszd a Pollákot!')
             time.sleep(0.5)
         else:
             GPIO.output(18, False)

         button_state = GPIO.input(20)
         if button_state == False:
             GPIO.output(25, True)
             print('Kék led világít!')
             time.sleep(0.5)
         else:
             GPIO.output(25, False)
         button_state = GPIO.input(21)
         if button_state == False:
             # Reading the DHT11 is very sensitive to timings and occasionally
             # the Pi might fail to get a valid reading. So check if readings are valid.
            for x in range(1):
                if humidity is not None and temperature is not None:
                    for x in range(10):
                        GPIO.output(18, GPIO.HIGH)
                        t
                        GPIO.output(18, GPIO.LOW)
                        t
                        GPIO.output(23, GPIO.HIGH)
                        t
                        GPIO.output(23, GPIO.LOW)
                        t
                        GPIO.output(24, GPIO.HIGH)
                        t
                        GPIO.output(24, GPIO.LOW)
                        t
                        GPIO.output(25, GPIO.HIGH)
                        t
                        GPIO.output(25, GPIO.LOW)
                        t
                        GPIO.output(24, GPIO.HIGH)
                        t
                        GPIO.output(24, GPIO.LOW)
                        t
                        GPIO.output(23, GPIO.HIGH)
                        t
                        GPIO.output(23, GPIO.LOW)
                        t

                        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(Hőmérséklet, Páratartalom))
                else:
                        print('Failed to get reading. Try again!')

                time.sleep(0.5)          
except:
    GPIO.cleanup()
