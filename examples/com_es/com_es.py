import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

user_id = 0
enroll_option = 0x79 #AUTO ID

module.send_command(command=pysfm.UF_COM_ES, param=user_id, size=0, flag=enroll_option)

# Response of first fingerprint imagescanning
module.read_response_command(10)    # If Scan success option in system parameter is enabled, 
module.read_response_command(10)  

# Response of second fingerprint image scanning
module.read_response_command(10)    # If Scan success option in system parameter is enabled, 
module.read_response_command(10)
module.disconnect()
print ('<< End')