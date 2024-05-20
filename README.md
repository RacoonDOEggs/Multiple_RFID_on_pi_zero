# Multiple_RFID_on_pi_zero
I figured out how to read multiple MFRC522 RFID readers with the raspberry pi zero 2w. Here's how I did it.



For a project I had I needed to sequentially read multiple MFRC552 RFID reader modules. However, the pi zero 2w has a hardcoded CS pin and these modules need to send multiple messages back and forth in order to give the information from the tag. I didn't find a one stop shop with all the information needed to achieve this, so here's a guide to show how I did it with the help from [@Zach3292](https://github.com/Zach3292).

## Parts Used
1. Raspberry-pi zero 2w
2. ADG728 I2C analog switch from [Adafruit](https://www.adafruit.com/product/5899)
3. 3 MFRC522 modules, but you can use up to 8

## Connections
To connect the MFRC522's to the Pi, I recommend following this great guide by [PiMyLifeup](https://pimylifeup.com/raspberry-pi-rfid-rc522/)

The SDA and SCL of the ADG728 are connected to pins 3 and 5 of the pi respectively (I2C channel 1).

Connect pin24 (CE0) of the pi to pin D of the ADG728. You can then take the various S# pins to connect the various SDA (CS) pins of the MFRC522 modules. Add 10k pull-up resistors to the S# pins as they are floating when not enabled by the chip.

The other pins of the SPI bus (MOSI, MISO, SCK) are connected in parallel as shown in the PiMyLifeUp tutorial.

Connect the ADG728 VIN to 3.3v as well as the RST pin.

## Building and launching the project
I did not package the docker image, but you can build it from the root directory of the project with docker using this command:
```bash
$ sudo docker container built -t "[give it a cute name]" -f RPI-RFID/Dockerfile
```

Then, make sure you have both SPI and I2C enables in your pi's configuration using:
```bash
$ sudo raspi-config
```
and turning them on in `Interface options`.
Alternatively you can always use dtparam:
```bash
$ sudo dtapram spi=on/off
$ sudo dtapram i2c=on/off
```

You then need to run the container in privileged mode so it can access the communication chanels using the command:
```bash
$ sudo docker container run --privileged -d [the cute name you gave it earlier]
```
You can finally see the output by using docker logs:
```bash
$ sudo docker logs -f [the long string that appeared uppon startup of the container]
```

## ADG728 on pi
The ADG728 did not have a library for use on the pi, so I made a quick one that allows the use of 3 functions:
1. `flip(switch:int)`
	This command allows you to slip the state of the given S# 	pin. (S1 = 0, S2 = 1, etc...)
2. `set_bits(states:int)`
	This sets the state of all the switches using an 8 bit 	integer. (Ex: 15 = '00001111' will connect S1,S2,S3 and 	S4.)
3. `reset()`
	This sets all the bits to 0. All the switches are opened.

### MAKE SURE YOU ONLY HAVE ONE SWITCH ENABLED AT A TIME WHEN USING THIS CHIP TO SELECT BETWEEN CS PINS TO AVOID CROSSTALK!!! (unless that is what you want for your application)


## MFRC522 library
The library provided in this project is a modified version of the [PiMyLifeUp library](https://github.com/pimylifeup/MFRC522-python).
However, while testing, I found that my SPI bus was a bit unstable with jumper connections so I lowered the speed by 25%.

## Docker Container
Another though part of this project was figuring out the right configuration for the docker container. 
You don't have to use the Dockerfile provided here, but make sure yours includes the following dependencies for this to work:
1. `RPI.GPIO`
2. `spidev`
3. `smbus` 
4. `i2c-tools` (I have found you can't install i2c-tools with apt-get unless you run apt-get update beforehand)

### MAKE SURE YOU COPY THE CUSTOM LIBRARIES BEFORE TRYING TO INSTALL THEM WITH `pip install -e`!!!


I believe this is all I needed to figure out during this project. If anything is unclear do not hesitate to file an issue to ask your questions.
