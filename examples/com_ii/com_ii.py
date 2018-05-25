import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')


f = open('fp_image.raw', 'rb')
data = f.read()
data_list = []

for x in data:
    data_list.append(ord(x))

f.close()

image_size = len(data_list)

# Identify by image
module.send_command(command=pysfm.UF_COM_II, param=0, size=image_size, flag=0)
module.send_data(data_list) # Send fingerprint image data
module.send_end_packet() 

module.read_response_command()  # If Scan success option in system parameter is enabled,  
module.read_response_command()

print ('<< End')