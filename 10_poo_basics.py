# 
# POO basics
#
#	Class:
#		- Syntax:
#			class ClassName:
#				(... object_properties ...)

#				def __init__(self): # constructor
#					# if a prop starts with '__', it's encapsulated (private),
#					# which means it cannot be accessed (get/set) from outside
#					(... code to execute when an instance is created, generally initial_status_properties ...)

#				def __del__(self): # destructor
#					(... code to execute when an instance is destroyed, for example, logging tasks ...)

#				def __str__(self): # redefine str(); automatically called
#					(... code to execute when a string representation of the object is required ...)

#				def __len__(self): # redefine len()
#					(... code to execute when a custom len property for the object is required ...)

#				(... object methods ...) # they receive 'self' as param
#				(... object functions ...) # they don't receive 'self'; static methods
#
#	Object (class' instance):
#		- Syntax:
#			object_name = ClassName()
#
from modules.vehicles import Car

print("----------------------- Cars -----------------------")

my_car = Car('001', 440, 210, "cm")  # calling the constructor
print(my_car)  # initial status
print()

my_car.turn(True)  # status it's encapsulated, but can be modified with methods
my_car.longitude = 510  # accessible, because it's not encapsulated
print(my_car)
print()
# second time we try to turning it ON, it's already ON, so it fails to default value (parked)
my_car.turn(True)
print(my_car)
print()
del my_car
