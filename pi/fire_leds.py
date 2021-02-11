import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

for i in range(0):
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)


# Endlosschleife
while True:
    if GPIO.input(24) == 0:
        # Ausschalten
        GPIO.output(23, GPIO.LOW)
    else:
        # Einschalten
        GPIO.output(23, GPIO.HIGH)
