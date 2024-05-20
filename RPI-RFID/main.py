import RPi.GPIO as GPIO
from time import sleep, time
from mfrc522 import SimpleMFRC522
from adg728 import ADG728

switch = ADG728()

rfid = SimpleMFRC522()

#Set the time spent trying to read each reader
readDelay = 1
#Set the amount of readers used
sensorNb = 3

lastReading:int = []
for i in range(sensorNb):
    lastReading.append(0)

def readRFID(sensorNb):
    switch.flip(sensorNb)

    currentTime = time() 
    id, text = rfid.read_no_block()
    while (not id) and (time()-currentTime < readDelay):
        id, text = rfid.read_no_block()

    switch.reset()
    return id, text 

try:
    while True:
        switch.reset()
        for i in range(sensorNb):
            tempReading, _ = readRFID(i)
            print('Sensor ' + str(i) + ' : ' + str(tempReading))
            lastReading[i] = tempReading
        sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

