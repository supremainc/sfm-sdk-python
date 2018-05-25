import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

f = open('template.dat', 'rb')
data = f.read()
data_list = []

for x in data:
    data_list.append(ord(x))

f.close()

template_size = len(data_list)

# Identify by template
module.send_command(command=pysfm.UF_COM_IT, param=0, size=template_size, flag=0)
module.send_data(data_list)
module.send_end_packet()
module.read_response_command() # If Scan success option in system parameter is enabled,  
module.read_response_command()

print ('<< End')