import RPi.GPIO as GPIO
import time

#configure i/o pins
#GPIO.setmode(GPIO.BCM)
button_pin = 26
buzzer_pin = 18

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        # check if button pressed
        if(GPIO.input(button_pin) == 0):
            # set buzzer on
            GPIO.output(buzzer_pin, GPIO.HIGH)
        else:
            # it's not pressed, set button off
            GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()