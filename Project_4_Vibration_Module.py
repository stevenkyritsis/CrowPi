#Use right set of switches
import RPi.GPIO as GPIO
import time

vibration_pin = 13

GPIO.setmode(GPIO.BOARD)

#turn on vibration
GPIO.setup(vibration_pin, GPIO.HIGH)

#wait half a second
time.sleep(3)

#turn off vibration
GPIO.output(vibration_pin, GPIO.LOW)

#cleanup GPIO
GPIO.cleanup()
