# tester file

from constants import REGISTERS
import register_store

def test_header():
    if register_store.get_register_value(65001)==1768973671:
        print("URR functionality is present")
        return True
    else:
        print("URR functionality is absent")
        return False
    
def output_URR_version():
    print("URR Version:", register_store.get_register_value(65003))
    






    