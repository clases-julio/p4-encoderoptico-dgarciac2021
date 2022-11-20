#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)

in1_pin = 23
in2_pin = 24
button_pin = 21
encoder_pin = 16

GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(in2_pin, False)

MOTOR = GPIO.PWM(23, 100)
MOTOR.start(0)

RPM_PRINT_TIMER = 0.250
RPM_PRINT_PREV_TIME = 0
COUNTER = 0

def callbackEncoder(channel)

def callbackExit(signal, frame)

def calculateRPM()

def driveMotor()

def main():

    GPIO.add_event_detect(encoder_pin, GPIO.RISING, callback=callbackEncoder, bouncetime=1)

    print("CTRL + C to exit!", end="\n\n")

    while True:
        if (time.time() - RPM_PRINT_PREV_TIME >= RPM_PRINT_TIMER):
            print("                                        ", end="\r")
            print("RPM: ", int(calculateRPM()), end="\r")
            COUNTER = 0
            RPM_PRINT_PREV_TIME = time.time()

        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

callbackEncoder(channel):
    global COUNTER
    COUNTER += 1

driveMotor():
    if (not GPIO.input(button_pin)): MOTOR.ChangeDutyCycle(50)
    else: MOTOR.ChangeDutyCycle(0)

callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

calculateRPM():
    global COUNTER
    global RPM_PRINT_TIMER

    return (COUNTER * 60) / RPM_PRINT_TIMER

if __name__ == "__main__":
    main()
