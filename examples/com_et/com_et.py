import pysfm
import io
import time

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

user_id = 123456
# Enroll by template
module.send_command(command=pysfm.UF_COM_ET, param=user_id, size=384, flag=0x79)

module.send_data(data)
module.send_end_packet()
module.read_response_command(1) # If Scan success option in system parameter is enabled,  
module.read_response_command(1)

param = module.response_command.param
size = module.response_command.size
error = module.response_command.error

print ('UserID : %d , The number of features : %d , Error : 0x%02X' % (param, size, error))

print ('<< End')

module.disconnect()