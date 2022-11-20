#!/usr/bin/env python3

import RPi.GPIO as io
import time
import signal
import sys

io.setmode(io.BCM)

in1_pin = 23
in2_pin = 24
button_pin = 21
encoder_pin = 16

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

counter = 0

def callbackEncoder(channel):
    global counter
    counter += 1

io.setup(button_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(encoder_pin, io.IN, pull_up_down=io.PUD_UP)
io.add_event_detect(encoder_pin, io.RISING, callback=callbackEncoder, bouncetime=100)

motor = io.PWM(23, 100)
motor.start(0)

io.output(in2_pin, False)

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    io.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

while True:
    if (not io.input(button_pin)): motor.ChangeDutyCycle(50)
    else: motor.ChangeDutyCycle(0)
    print(counter)
    signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C
