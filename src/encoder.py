#!/usr/bin/env python3

###############################################################################
# encoder.py                                                                  #
#                                                                             #
# Authors: Ioana Carmen, Diego García                                         #
#                                                                             #
# This code will drive a motor through an H-Bridge and read the revolutions   #
# per minute of the axis.                                                     #
###############################################################################

###############################################################################
# Neccesary modules

import RPi.GPIO as GPIO
import time
import signal
import sys

###############################################################################
# Pinout management

GPIO.setmode(GPIO.BCM)

in1_pin = 23
in2_pin = 24
button_pin = 21
encoder_pin = 16

GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

###############################################################################
# Pinout initialization

GPIO.output(in2_pin, False)

MOTOR = GPIO.PWM(23, 100)
MOTOR.start(0)

###############################################################################
# Global variables

RPM_PRINT_TIMER = 0.250
pulseCounter = 0

###############################################################################
# Global methods

def callbackEncoder(channel):
    global pulseCounter # the label 'global' links this local variable to the
    # homonymous global variable 
    pulseCounter += 1

def driveMotor():
    if (not GPIO.input(button_pin)): MOTOR.ChangeDutyCycle(50)
    else: MOTOR.ChangeDutyCycle(0)

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

def calculateRPM():
    global pulseCounter
    global RPM_PRINT_TIMER
    # We assume a linear behaviour for the motor and follow this formula:
    return (pulseCounter * 60) / RPM_PRINT_TIMER

###############################################################################
# Main program

def main():

    GPIO.add_event_detect(encoder_pin, GPIO.RISING, callback=callbackEncoder)
    # Detect rising edge in the encoder pin.

    print("CTRL + C to exit!", end="\n\n")
    # with 'end' the final of each 'print' could be customized.

    global pulseCounter
    rpmPrintPrevTime = 0 # Set a time milestone.

    while True:

        driveMotor()
        # if the actual time sub the previous time is larger than
        # the set time, means that the timer has expire.
        if (time.time() - rpmPrintPrevTime >= RPM_PRINT_TIMER):
            print("                                        ", end="\r")
            print("RPM: ", int(calculateRPM()), end="\r")
            pulseCounter = 0
            rpmPrintPrevTime = time.time() # refresh the actual time for the
            # next iteration

        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

###############################################################################

if __name__ == "__main__":
    main()
