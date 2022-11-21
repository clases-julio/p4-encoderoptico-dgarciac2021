# P4-encoderOptico

This exercise consists on read the RPM of a spinning wheel using software [interruptions](https://github.com/clases-julio/p3-interruptions-dgarciac2021/wiki/Interrupt). For this particular exercise, we are using a DC motor attached to a custom-designed holder to rotate the wheel. Furthermore, in order to drive such motor an additional driver is added to the circuit. You might want to take a look on the wiki, since there is info of everything involved on this project. From the motor to the motor to the driver.

## Motor Holder

## Circuit Assembly

With the addition of the DC motor driver, wiring could became a little bit messy and more complex than previous exercises. We are using one [button](https://github.com/clases-julio/p3-interruptions-dgarciac2021/wiki/Button), one driver, one 330Ω resistor and the ITR8102 sensor provided with out Raspberry Pi kits.[^1]

This is an schematic made with [Fritzing](https://fritzing.org/):

![Schematic](./doc/img/schematic.png)

And this is the real circuit!

![aerial view](./doc/img/aerial-view.jpg)

## Code

We would like to highlight some remarkable aspects from our code.

## Circuit testing

This is the result! Pretty nice, isn't it?

![Circuit test](./doc/img/rpmDemoL.gif)
![Circuit test](./doc/img/rpmDemoT.gif)

[^1]: The ITR8102 is not listed on the Fritzing libraries, so another alternative with identical wiring is used to represent it.
