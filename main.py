#  main file

import test_file
import register_store
import conversions


if register_store.establish_connection(): # check connection to Modbus server
    
    register_store.update_registers() # attempt to read in all URRs

    if test_file.test_header(): # check for URR implementation

        register_store.check_registers() # check all registers

        test_file.output_URR_version() # output URR version

        test = conversions.dec_to_string(register_store.get_register_value(65001)) # read URR string using specified encoding
        print(test)
       
        # test
        print(test)
    


    else:
        print("Exiting due to missing URR functionality")

else:
    print("Exiting due to connection failure")



