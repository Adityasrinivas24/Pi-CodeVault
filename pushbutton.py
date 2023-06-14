import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
# Connect NO or NC contact to GPIO 17
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)  # Connect LED to GPIO 27

while True:
    input_state = GPIO.input(17)  # Read input state of switch ,physical pin 17 
    if input_state == False:  # Switch is pressed
        GPIO.output(27, GPIO.HIGH)  # Turn on LED , Physical pin 13  
    else:  # Switch is not pressed
        GPIO.output(27, GPIO.LOW)  # Turn off LED
    sleep(0.1)  # Small delay to avoid multiple button presses
