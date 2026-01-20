#  comment

from pymodbus.client.tcp import ModbusTcpClient  # explicit import works in latest version

IP_Address = '10.1.140.2' # IP address of the Modbus server
client = ModbusTcpClient(IP_Address, port=502)


if client.connect(): # Check if connection is successful
    print("Connected successfully")

    registers = [
        (65001, 2), (65003, 1), (65004, 1), (65005, 1), (65006, 1), (65007, 1),
        (65008, 1), (65009, 2), (65011, 2), (65013, 2), (65015, 1), (65016, 1),
        (65017, 2), (65019, 2), (65021, 2), (65023, 2), (65025, 1), (65026, 1),
        (65027, 1), (65028, 1), (65029, 1), (65030, 1), (65031, 2), (65033, 2),
        (65035, 2), (65037, 2), (65039, 2), (65041, 2), (65043, 2)
    ]

    failed = []
    for addr, count in registers:
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


