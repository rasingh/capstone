#!/usr/bin/env/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

print("SYS: Raspberry Pi Initializing")

# Setup GPIO Port pin 12 as an input (could optionally configure pull up/down)
GPIO.setup(12, GPIO.IN)

# Loop forever constantly checking the input pin to see if it has been brought low
while True:
    input_value = GPIO.input(12)        # Read the status of input Pin 12
    if input_value == False:            # If the pin is low (i.e. button has been pushed)
                print("\n\n\nTrigger: CLICK PICTURE\n")

    else: print("waiting...")
    while input_value == False: # Keep checking status of pin until it is no longer low
        input_value = GPIO.input(11)

# We never get here, but if we did, we should do this

# Return all GPIO pins back to their default state of being inputs with no pull up/down
GPIO.cleanup()
