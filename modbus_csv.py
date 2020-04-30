#!/usr/bin/python
import minimalmodbus
import csv

def init_csv():
    # the a is for append, if w for write is used then it overwrites the file
    with open('sensor_readings.csv', mode='a') as sensor_readings:
        sensor_write = csv.writer(sensor_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_log = sensor_write.writerow(['ADD00','ADD01','ADD02','ADD03','ADD04','ADD05','ADD06','ADD07','ADD08','ADD09','ADD10'])
        return(write_to_log)

def write_data_csv(data):
    # the a is for append, if w for write is used then it overwrites the file
    with open('sensor_readings.csv', mode='a') as sensor_readings:
        sensor_write = csv.writer(sensor_readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_log = sensor_write.writerow(data)
        return(write_to_log)

instrument = minimalmodbus.Instrument('/dev/ttyUSB2', 1)  # port name, slave address (in decimal)
instrument.serial.baudrate = 9600         # Baud
instrument.serial.timeout = 0.2
instrument.mode = minimalmodbus.MODE_RTU
init_csv()

data_set = []
for i in range(10):
    data_set.append(instrument.read_register(i, 1))
print(data_set)
write_data_csv(data_set)



## Change temperature setpoint (SP) ##
## NEW_TEMPERATURE = 95
## instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
