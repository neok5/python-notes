#
# POO inheritance (II)
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
class Vehicle:

	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		self.moving = False
		self.speeding_up = False
		self.breaking = False

	def turn_on(self):
		self.moving = True

	def speed_up(self):
		self.speeding_up = True

	def break_(self):
		self.breaking = True

	def status(self):
		print(f"""Brand: {self.brand}, Model: {self.model}\n[Moving: """
		f"""{self.moving}]\n[Speeding up: {self.speeding_up}]\n[Breaking: {self.breaking}]""")

class ElectricVehicle(Vehicle):

	battery_life = 0
	loading = False

	def __init__(self, brand, model):
		super().__init__(brand, model)
		self.battery_life = 100

	def load_energy(self):
		self.loading = True

class ElectricBicycle(ElectricVehicle, Vehicle):
	pass

class Car:

	def movement(self):
		print("I'm moving with 4 wheels")

class Motorbike:

	def movement(self):
		print("I'm moving with 2 wheels")

class Truck:

	def movement(self):
		print("I'm moving with 6 wheels")

def vehicle_movement(vehicle):
	vehicle.movement()

print("----------------------- Electric bicycles -----------------------")

electric_bicycle = ElectricBicycle("Xiaomi", "QCycle")
electric_bicycle.status()
print(f"\nIs an electric bicycle also a vehicle? {isinstance(electric_bicycle, Vehicle)}")
print()

print("----------------------- Vehicle polymorphism -----------------------")

vehicle_movement(Motorbike()) # method's implementation called depends on the object type
vehicle_movement(Car())
vehicle_movement(Truck())
print()