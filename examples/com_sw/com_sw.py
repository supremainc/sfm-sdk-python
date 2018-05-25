import pysfm
import serial

print pysfm.__version__

module = pysfm.Module("COM6")

if module.connect() == False:
    exit(-100)

print ('Start >>')

parameter_id = pysfm.UF_SYS_TIMEOUT
parameter_value = 0x33

# Read system parameter
module.send_command(command=pysfm.UF_COM_SR,param=0, size=0, flag=parameter_id)
module.read_response_command()
old_value = module.response_command.size

# Write system parameter
module.send_command(command=pysfm.UF_COM_SW, param=0, size=parameter_value, flag=parameter_id)
module.read_response_command()

# Read system parameter
module.send_command(command=pysfm.UF_COM_SR,param=0, size=0, flag=parameter_id)
module.read_response_command()
written_value = module.response_command.size

if parameter_value == written_value:
    print('Written Success')

# Roll back system parameter
module.send_command(command=pysfm.UF_COM_SW, param=0, size=old_value, flag=parameter_id)
module.read_response_command()

# Read system parameter
module.send_command(command=pysfm.UF_COM_SR,param=0, size=0, flag=parameter_id)
module.read_response_command()
written_value = module.response_command.size

if old_value == written_value:
    print('Rollback Success')

print ('<< End')