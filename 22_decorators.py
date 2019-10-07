#
# DECORATORS
#
#	- They are functions that add functionalities to another functions.
#	 Their basic structure is composed by 3 functions (A, B and C) where A receives B
#	  and returns another function C. A decorator always returns a function. Syntax:
#
#			# 'decorator_function' is A, 'function' is B and 'internal_function' is C
#			def decorator_function(function):
#				def internal_function():
#					# internal function implementation
#				return internal_function
#
#	- To decorate a 'function' with a 'decorator_function' we have to annotate
#	 the 'function' declaration desired with the annotation '@decorator_function'.
#
def log_decorator(function):
	def apply_log():
		print('\tCalculating result...', end = ' ')
		print(function())
		print('\tCalculation done.')
		print()
	return apply_log

def log_decorator_w_params_and_keyword_params(function):
	# with '*' it receives all arguments regardless how many they are
	# using '**' is the same for keywords params
	def apply_log(*args, **kwargs):
		print('\tCalculating result...', end = ' ')
		print(function(*args, **kwargs))
		print('\tCalculation done.')
		print()
	return apply_log

@log_decorator
def _sum():
	return 23 + 5

@log_decorator
def _sub():
	return 32 - 5

@log_decorator_w_params_and_keyword_params
def _pow(base, exponent):
	return pow(base, exponent)

print("---------------------- Decorating calculations (basic) -----------------------\n")

_sum()
_sub()

print("---------------------- Decorating calculations (advanced) -----------------------\n")

keyword_params = { 'exponent' : 10, 'base' : 2 }
_pow(**keyword_params)