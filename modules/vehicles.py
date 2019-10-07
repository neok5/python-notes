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

class ElectricBicycle(ElectricVehicle, Vehicle):
	pass

class Cab:

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

class Car:

	def __init__(self, longitude, width, size_unit):
		self.longitude = longitude  # 'public'
		self.width = width  # 'public'
		self.__size_unit = size_unit  # 'private'
		self.__status = "parked"  # 'private'

	def turn(self, status):  # 'public'
		self.__status = "moving" if status and self.__internal_check(status) else "parked"

	def show_status(self):  # 'public'
		return f'Car size is {self.longitude}x{self.width} {self.__size_unit} and is {self.__status}'

	def __internal_check(self, given_status):  # 'private'
		print("Doing internal check... [status change]")
		return self.__status == "parked" if given_status else "moving"