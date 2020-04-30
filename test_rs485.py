#!/usr/bin/python
import serial
import time

ser = serial.Serial(
    port='/dev/ttyUSB2',
    baudrate=115200,
    timeout=1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.flushOutput()
ser.flushInput()

rx_counter=0
tx_counter=0
while True:
    tx_counter=tx_counter+1
    ser.write("Tx counter = %d | Rx counter = %d\n\r" % (tx_counter,rx_counter))
    print("Tx counter = %d | Rx counter = %d" % (tx_counter,rx_counter))

    a=ser.read(1)

    if a:
        rx_counter=rx_counter+1
        ser.write("Tx counter = %d | Rx counter = %d | Received: %s %02x\n\r" % (tx_counter,rx_counter,a,ord(a)))
        print("Tx counter = %d | Rx counter = %d | Received: %s %02x" % (tx_counter,rx_counter,a,ord(a)))
