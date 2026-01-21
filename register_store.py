# FILE TO COMMUNICATE WITH MACHINE USING MODBUS

from constants import REGISTERS
from config import MODBUS_IP, MODBUS_PORT
from pymodbus.client.tcp import ModbusTcpClient  # explicit import works in latest version
import math
import conversions
client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
registers_data = []

def establish_connection():
    if client.connect(): # Check if connection is successful
        print("Connected successfully to IP Address",MODBUS_IP)
        return True;
    else:
        print("Unable to connect")

    client.close()


def check_registers():
    if client.connect():
        registers_data.clear()
        failed = []
        for addr, count in REGISTERS:
            result = client.read_holding_registers(address=addr, count=count)
            if result.isError():
                print(f"Error reading address {addr}: {result}")
                failed.append(addr)
            else:
                print(f"Address {addr}:", result.registers)
                registers_data.append([addr,count,result.registers])
                
        if not failed:
            print("All registers read successfully via Modbus")
        else:
            print("Failed registers:", failed)

    else:
        print("Unable to connect")

def update_registers():
    if client.connect():
        registers_data.clear()
        for addr, count in REGISTERS:
            result = client.read_holding_registers(address=addr, count=count)
            if result.isError():
                return
            else:
                registers_data.append([addr,count,result.registers])              
    else:
        return


def get_register_value(register_num):
    for reg_num, reg_size, reg_value in registers_data:
        if reg_num == register_num:
            if reg_size == 1:
                return reg_value[0]
            elif reg_size == 2:
                return (reg_value[1] << 16) + reg_value[0]
            return reg_value
    # Not found
    return -1

