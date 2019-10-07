'''contains a set of mathematical functions for quick use'''

class Number:
	'''represents a generic entity in the application'''
	def __init__(self, id):
		'''number's constructor, receives an id'''
		self.id = id

	def check_id(self):
		'''returns true if the id is into a valid range'''
		return 0 < self.id < 100

def sum(num_1, num_2):
	'''returns the result of adding both numbers'''
	print(f"Sum result is: {num_1 + num_2}")

def subtract(num_1, num_2):
	'''returns the result of subctract first number minus second one'''
	print(f"Subtract result is: {num_1 - num_2}")

def multiply(num_1, num_2):
	'''returns the result of multiply both numbers'''
	print(f"Multiplication result is: {num_1 * num_2}")