import pysfm
import serial
import time

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

user_id = 1

# Verify by scan
module.send_command(command=pysfm.UF_COM_VS, param=user_id, size=0, flag=0)
module.read_response_command()  # If Scan success option in system parameter is enabled,  
module.read_response_command()


print ('<< End')