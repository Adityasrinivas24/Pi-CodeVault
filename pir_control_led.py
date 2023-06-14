import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pir1 = 10
pir2 = 23
green = 15
red = 18

GPIO.setup(pir1,GPIO.IN)
GPIO.setup(pir2,GPIO.IN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)


while True:
    if GPIO.input(pir1):
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(red, GPIO.LOW)  # Turn off the red LED
    elif GPIO.input(pir2):
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(green, GPIO.LOW)  # Turn off the green LED
