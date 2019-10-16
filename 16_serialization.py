#
# SERIALIZATION
#
#	- It's the process of translating a data structure or an object state into a format
#	  that can be stored (file, buffer) or transmitted (through a network) and reconstructed.
#	  The format can be a binary stream (most common case) or also even XML/JSON.
#
#	- To handle binary files, we have to use built-in Python module 'pickle'
#	  'pickling' - process whereby a Python object is converted into a bytestream
#	  'unpickling' - inverse process whereby a bytestream is converted back into an object
#
#	- Module 'pickle' utilities:
#		· dump(data, file) - dump specified data into specified file
#		· load(file) - load and return specified file content (and can be set to a var)
#			module that loads the objects must know about object types it's loading, like
#			user-defined object types, in order to be able to handle and reconstruct them
#
from pickle import dump, load
filename_list = '16_namelist_bfile'

print("----------------------- Scientific name list (dump) ------------------------")

name_list = ['Albert', 'Marie', 'Nikola']
new_binary_file = open(filename_list, 'wb')
# opening files in binary mode creates a '_io.BufferedWriter'
print(f'{type(new_binary_file)}')
print(f'Content to write to namelist file: {name_list}\nDumping...')
dump(name_list, new_binary_file)
new_binary_file.close()
del new_binary_file
print()

print("----------------------- Scientific name list (load) ------------------------")

recov_binary_file = open(filename_list, 'rb')
print(f'Loading...')
recov_name_list = load(recov_binary_file)
recov_binary_file.close()
del recov_binary_file
print(f'Recovered content from namelist file: {recov_name_list}')
print()





from modules.vehicles import Vehicle
filename_object = '16_carobjects_bfile.pckl'  # we can open .pckl files with Sublime Text for a binary perspective

print("----------------------- Vehicle object (dump) ------------------------")

my_vehicle_1 = Vehicle('Acura', 'RSX')
my_vehicle_2 = Vehicle('Nissan', 'Leaf')
print('Vehicles to serialize (as list)\n')
my_vehicle_1.break_()
my_vehicle_1.status()
print()
my_vehicle_2.break_()
my_vehicle_2.status()

vehicle_list = [my_vehicle_1, my_vehicle_2]
cars_bfile = open(filename_object, 'wb')
print('\nDumping...')
dump(vehicle_list, cars_bfile)
cars_bfile.close()
del cars_bfile
print()

print("----------------------- Vehicle object (load) ------------------------")

recov_cars_bfile = open(filename_object, 'rb')
print('Loading...\n')
recov_vehicle_list = load(recov_cars_bfile)
recov_cars_bfile.close()
del recov_cars_bfile
print(f'Recovered content from carobject file:\n')
recov_vehicle_list[0].status()
print()
recov_vehicle_list[1].status()
print()