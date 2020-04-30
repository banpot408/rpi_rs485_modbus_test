#!/usr/bin/python
import minimalmodbus

#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
#instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)  # port name, slave address (in decimal)
#instrument = minimalmodbus.Instrument('/dev/ttyUSB2', 1)  # port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB3', 1)  # port name, slave address (in decimal)


instrument.serial.baudrate = 9600         # Baud
instrument.serial.timeout = 0.2
instrument.mode = minimalmodbus.MODE_RTU

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(1, 10)  # Registernumber, number of decimals
print(temperature)

data_set = []
for i in range(10):
    data_set.append(instrument.read_register(i, 1))
print(data_set)



## Change temperature setpoint (SP) ##
## NEW_TEMPERATURE = 95
## instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
