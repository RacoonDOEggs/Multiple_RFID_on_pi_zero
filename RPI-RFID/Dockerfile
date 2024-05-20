FROM python:3-bookworm

COPY RPI-RFID/main.py ./
COPY MFRC522-python ./MFRC522-python 
COPY ADG728-python ./ADG728-python

RUN pip install --no-cache-dir RPi.GPIO spidev smbus
RUN pip install -e ./MFRC522-python 
RUN pip install -e ./ADG728-python

RUN apt-get update -y
RUN apt-get install -y i2c-tools

CMD ["python3", "-u", "./main.py"]
