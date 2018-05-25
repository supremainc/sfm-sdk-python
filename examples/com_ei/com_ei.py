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

user_id = 0
enroll_option = 0x79 #AUTO ID
image_size = 272*320


# Enroll by image
module.send_command(command=pysfm.UF_COM_EI, param=user_id, size=image_size, flag=enroll_option)    # image width : 272 , image width : 320. These values can be differenciated according to type of SFM products.
module.send_data(data_list)
module.send_end_packet()
module.read_response_command()  # If Scan success option in system parameter is enabled, 
module.read_response_command() 

print ('<< End')