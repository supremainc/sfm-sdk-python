import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

# Identify by scan
module.send_command(command=pysfm.UF_COM_IS, param=0, size=0, flag=0)
module.read_response_command()  # If Scan success option in system parameter is enabled,  
module.read_response_command()

print ('<< End')