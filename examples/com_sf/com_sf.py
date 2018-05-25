import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

# Save system parameter
module.send_command(command=pysfm.UF_COM_SF)
module.read_response_command()

print ('<< End')