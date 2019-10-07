# 
# POO basics
#
#	Class:
#		- Syntax:
#			class ClassName:
#				(... object_properties ...)
#				def __init__(self): # constructor; 'self' = 'this' in Java
#					# if a prop starts with '__', it's encapsulated (private),
#					# which means it cannot be accessed (get/set) from outside
#					(... initial_status_properties ...)
#				(... object methods ...) # they receive 'self' as param
#				(... object functions ...) # they don't receive 'self'
#
#	Object (class' instance):
#		- Syntax:
#			object_name = ClassName()
#
from modules.vehicles import Car

print("----------------------- Cars -----------------------")

my_car = Car(440, 210, "cm")  # calling the constructor
print(my_car.show_status())  # initial status
print()

my_car.turn(True)  # status it's encapsulated, but can be modified with methods
my_car.longitude = 510  # accessible, because it's not encapsulated
print(my_car.show_status())
print()
# second time we try to turning it ON, it's already ON, so it fails to default value (parked)
my_car.turn(True)
print(my_car.show_status())
print()
