#
# POO inheritance (I)
#
#	How to build inheritance:
#		- Syntax:
#			class Subclass(Superclass):
#				{class body}
#
#	Method overloading:
#		- Syntax:
#			class Subclass(Superclass):
#				def name_method_in_superclass(self):
#					super().method_in_superclass() # call superclass method
#					{method body}
#
#		- As in majority of languages, this builds a inheritance operative chain, which
#		  starts from bottom to top, looking for the first implementation of the method
#
#	Multiple inheritance:
#		- Syntax:
#			class Subclass(Superclass1, Superclass2, ...)
#				{class body}
#
#		- The subclass inherits the constructor from first superclass (Superclass1)
#
#	Keyword super():
#		- In subclass constructor:
#			class Subclass(Superclass):
#				def __init__(self, ...superclass_const_params, ...subclass_cons_params):
#					super().__init__(superclass_constructor_params)
#					{ subclass initializations using subclass constructor params}
#
#		- In subclass methods:
#			def subclass_method(self):
#				super().superclass_method()
#				{ subclass method implementation }
#
#	Method isinstance():
#		- Python's utility that returns True if the instance belongs to the class
#			syntax: isinstance(object, class)
#			example: isinstance(my_car, Vehicle)
#
#	Polymorphism
#		- It's a programming language property that allows to send syntactically
#			identical messages to objects of different types. The only requirement
#			is that receiver must know how to handle and answer the message.
#
#
from modules.vehicles import *

print("----------------------- Vehicles -----------------------")

vehicle = Vehicle("Renault", "Megane")
vehicle.status()
print()

print("----------------------- Motorbikes -----------------------")

motorcycle = Motorcycle("Honda", "BCR")
motorcycle.status()
print()
motorcycle.do_wheelie()
motorcycle.status()
print()

print("----------------------- Vans -----------------------")

van = Van("VW", "1959")
van.status()
print()
print(van.load(True), end="\n\n")
van.turn_on()
van.status()
print()

print("----------------------- Electric bicycles -----------------------")

electric_bicycle = ElectricBicycle("Xiaomi", "QCycle")
electric_bicycle.status()
print(f"\nIs an electric bicycle also a vehicle? {isinstance(electric_bicycle, Vehicle)}")
print()

print("----------------------- Vehicle polymorphism -----------------------")

vehicle_movement(Motorbike())  # method's implementation called depends on the object type
vehicle_movement(Cab())
vehicle_movement(Truck())
