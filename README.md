# P4-encoderOptico

This exercise consists on read the RPM of a spinning wheel using software [interruptions](https://github.com/clases-julio/p3-interruptions-dgarciac2021/wiki/Interrupt). For this particular exercise, we are using a DC motor attached to a custom-designed holder to rotate the wheel. Furthermore, in order to drive such motor an additional driver is added to the circuit. You might want to take a look on the wiki, since there is info of everything involved on this project. From the motor to the motor to the driver.

## Motor Holder

![Schematic](./doc/img/frontSide.jpg)
![Schematic](./doc/img/backSide.jpg)

The motor holder showed above was designed specifically for this project. The software used was [Fusion 360](https://www.autodesk.com/products/fusion-360/). Although this is non-free propietary software, it is free for educational purposes as shown [here.](https://www.autodesk.com/products/fusion-360/education)

However the use of this holder was not that straight-forward, since apparently **some materials used on FDM printers** (Like PLA or ABS) **could became *invisible* for certains wavelengths, like the infrared ones**. In our case this made the sensor remain conductive despite of the wheel spinning in front of it. All details are covered in this [article.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208549/)

You can see how different materials behave with infrared radiation in this [video](https://www.youtube.com/watch?v=fpx7hsoYEt4), but with this frame you can get the idea:

![Infrared vs Visisble light through plastic](infraredVSvisible.png)

Fortunately, the solution for us was just use another brand of filament that can actually block the infrared light due to the pigments and impurities that the manufacturer added during the manufacturing process. That is why in the final images a different wheel is finally used. However this is not a practical solutions since it requires of an extensive trial/error process. It is also not consistent due to the same color can show differents behaviour between brands, or even different colors of the same manufacturer could be completly different on this terms.

Another consistent solution could be simply mask the wheel with some reflective material, like aluminum tape or similar. You can find all the 3D files [here.](https://github.com/clases-julio/p4-encoderoptico-dgarciac2021/tree/main/res/models)

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
