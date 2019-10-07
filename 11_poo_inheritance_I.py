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
#		- As in majority of languagues, this builds a inheritance operative chain, which
#		  starts from bottom to top, looking for the first implementation of the method
#
#	Multiple inheritance:
#		- Syntax:
#			class Subclass(Superclass1, Superclass2, ...)
#				{class body}
#
#		- The subclass inherits the constructor from first superclass (Superclass1)
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

class ElectricVehicle:

	battery_life = 0; loading = False

	def __init__(self):
		self.battery_life = 100

	def load_energy(self):
		self.loading = True

class Motorcycle(Vehicle):
	
	wheelie = "Two wheels on the ground"

	def do_wheelie(self):
		self.wheelie = "I'm doing a wheelie!"

	def status(self):
		super().status() # call the closest parent's method implementation
		print(self.wheelie)

class Van(Vehicle):

	full = False

	def load(self, full):
		self.full = full
		return "Van is full" if self.full else "Van is empty"

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
print(van.load(True), end = "\n\n")
van.turn_on()
van.status(); print()