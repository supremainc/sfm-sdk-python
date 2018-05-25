import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

# Delete all templates
module.send_command(command=pysfm.UF_COM_DA)
module.read_response_command()

print ('<< End')