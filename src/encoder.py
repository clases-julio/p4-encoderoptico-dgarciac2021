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
pulseCounter = 0

def callbackEncoder(channel):
    global pulseCounter
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

    return (pulseCounter * 60) / RPM_PRINT_TIMER

def main():

    GPIO.add_event_detect(encoder_pin, GPIO.RISING, callback=callbackEncoder, bouncetime=1)

    print("CTRL + C to exit!", end="\n\n")

    global pulseCounter
    rpmPrintPrevTime = 0

    while True:

        driveMotor()

        if (time.time() - rpmPrintPrevTime >= RPM_PRINT_TIMER):
            print("                                        ", end="\r")
            print("RPM: ", int(calculateRPM()), end="\r")
            pulseCounter = 0
            rpmPrintPrevTime = time.time()

        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

if __name__ == "__main__":
    main()
