import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

user_id = 1

# Delete template
module.send_command(command=pysfm.UF_COM_DT, param=user_id, size=0, flag=0)
module.read_response_command()

print ('<< End')