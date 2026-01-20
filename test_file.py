# tester file

from constants import REGISTERS
from config import MODBUS_IP, MODBUS_PORT
from pymodbus.client.tcp import ModbusTcpClient  # explicit import works in latest version

def read_registers():
    
    client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)


    if client.connect(): # Check if connection is successful
        print("Connected successfully")

        failed = []
        for addr, count in REGISTERS:
            result = client.read_holding_registers(address=addr, count=count)
            if result.isError():
                print(f"Error reading address {addr}: {result}")
                failed.append(addr)
            else:
                print(f"Address {addr}:", result.registers)

        client.close()

        if not failed:
            print("All registers read successfully")
        else:
            print("Failed registers:", failed)

    else:
        print("Unable to connect")
    