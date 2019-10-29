import math

class Test:
	def __init__(self):
		self.foo = 'foo'
		self._bar = '_bar'
		self.def_ = 'def_'  # use 'self.def' raises a SyntaxError, as 'def' is a keyword
		self.__dun = '__dun'  # name mangling converts '__dun' to '_Test__dun'

	@staticmethod
	def count_to_five():
		for _ in range(1, 6):  # '_' use as temporary varname
			print(_, end='\n' if _ == 5 else ' ')

# function len() | return the number of elements of the iterable
#				   it works if the iterable is a string (char list)
print("----------------------- len() -----------------------")
print(len(range(0, 2)))
print()

# function list(iterable) | convert the iterable into a list
# function tuple(iterable) | convert the iterable into a tuple
# the iterable can be a list, a tuple, a range, etc.
print("----------------------- list() and tuple() -----------------------")
my_tuple = ("Goku", 23, 5, 1992, "Goku")
my_list = list(my_tuple)
print(tuple(my_list))
print(list(my_tuple))
print()

# function int(str) | convert a 'str' into an 'int'
# function str(int | float) | convert a 'int' into an 'str'
print("----------------------- int() and str() -----------------------")
print(int("23"))
print(str(23.5))
print()

# shorter IF; ternary IF; syntax:
# 	'result_true' if 'condition' else 'result_false'
print("----------------------- shorter IF -----------------------")
age = 18
age_verification = True if age >= 18 else False
# if age >= 18:
# 	age_verification = True
# else:
# 	age_verification = False
print(age_verification)
print()

# math.modf(num) function
# return a tuple with 2 floats: (num) -> (decimal_part, integer_part)
# it can introduce some range error cause of precision
print("----------------------- math.modf() -----------------------")
decimal_num = 123.45
print(f"Number {decimal_num} | \
Decimal part {math.modf(decimal_num)[0]} | \
Integer part {math.modf(decimal_num)[1]}")
print()

# ord(str) | return an integer representing Unicode code for str
print("----------------------- ord() -----------------------")
print(f"Unicode for 'a' is {ord('a')}")
print(f"Unicode for 'b' is {ord('b')}")
print()

# iter(iterable) | return an iterator from a collection
# next(iterator[, default_value]) | return next element in an iterator
# 	if 'default_value' is specified, it's returned when the iterator ends
print("----------------------- iter() and next() -----------------------")
my_tuple = (1, 2, 3)
my_iterator = iter(my_tuple)
print("First element: " + str(next(my_iterator)))
print("Second element: " + str(next(my_iterator)))
print(f"Third element: {str(next(my_iterator))}")
print(next(my_iterator, "End of tuple"))
print()

# in functions, you can declare formal params with * as prefix
# 	- indicate an indeterminate number of params
#	- receive the params ('numbers') as a tuple
print("----------------------- * as formal params prefix -----------------------")
def return_numbers(*numbers):
	for number in numbers:
		yield number

# special case; a bit tricky
returned_numbers = return_numbers(1, 2, 3, 4, 5)
for n in returned_numbers:  # first 'next' element (1)(3)(5); excluded values
	# second 'next' element (2)(4)('\n'); printed values
	print(next(returned_numbers, "\n"), end=" ")
print()  # the loop fetch 2 values of generator per iteration

# you can also use a list as actual params in a function call
# this way, the '*' operator spreads the list and the function
# receives the params as separated arguments instead of a list
print("----------------------- * as actual params prefix -----------------------")
print(list(range(3, 6)))            # normal call with separate arguments = [3, 4, 5]
args = [3, 6]
print(list(range(*args)), '\n')            # call with arguments unpacked from a list = [3, 4, 5]

# KEYWORD PARAMS (arguments passed using its formal param name)
# you can also declare formal params with '**' when they are keyword ones
print("----------------------- ** as formal and actual params prefix -----------------------")
def local_pow(base, exponent):
	return pow(base, exponent)

def _pow(*args_, **kwargs):
	return local_pow(*args_, **kwargs)

print(f'\tPow with ordered params: {_pow(2, 10)}')
keyword_arguments = {'exponent': 10, 'base': 2}
print(f'\tPow with unordered params (using keywords): {_pow(**keyword_arguments)}\n')

# function print() with param keywords
#	'sep' - printed elements separator; default value: ' '
# 	'end' - indicates the 'str' printed at last; default value: '\n'
#		useful when you want to avoid the line feed ('\n') of print()
#	'file' - object with write(string) method; default value: 'sys.stdout'
#		it could be an opened file to write in it
print("----------------------- print() with keywords -----------------------\n")

print("word one", "word two", "word three", sep='')
print("word one", "word two", "word three", sep=' | ')
print("word one", "word two", "word three", sep='\t')
print("word1", end='')  # removes the line feed
print('\n')  # used with '\n' to compensate line just above

# WITH statement | used in exception handling, specially with open resources
#	(same as 'try-with-resources' from Java 8)
#
# 	Syntax:
#		with function_call() as function_call_result_alias:
#			sentence_to_handle_resource_that_may_raise_exception
#
# Without 'with' -forgive the repetition-, we had to write something like:
#	opened_file = open('file_path', 'r')
#	try:
#		opened_file.read()
#	except CaughtException as e:
#		error_handling # here 'e' can be used as the exception variable
#	finally:
#		opened_file.close()
print("----------------------- 'with' and 'pass' -----------------------")

print()
try:
	with open('file_path', 'r') as opened_file:
		data = opened_file.read()  # it closes the resource itself
except FileNotFoundError as e:
	print(f"Exception raised:\n\t{e}")

# PASS statement | is a null operation; when is executed, nothing happens
# 				   useful as placeholder when a statement is required syntactically
class ClassNotImplementedYet:
	pass

	def function_not_implemented_yet(self):
		pass

print()

# UNDERSCORES | they have 5 principal uses or patterns:
#
#	* single leading underscore ['_var']
#		- by convention, indicates the element isn't intended to be accessed externally
#		- do impact how names get imported from modules:
#			+ using wildcard imports (from module import *), Python doesn't import them
#			+ using normal imports (import module), Python does import them
#
#	* single trailing underscore ['var_']
#		- by convention, useful to avoid name conflicts with Python keywords
#
#	* double leading underscore (and at most 1 trailing) ['__var']
#		- in inheritance, useful to avoid accidental overloading with superclasses
#		- triggers 'name mangling': inside class 'FooBar', '__boo' becomes '_FooBar__boo')
#
#	* double leading and trailing underscore ['__var__']
#		- 'name mangling' is not applied, as it has double trailing underscore (>= 2)
#		- are reserved for special use in the language ('magic methods'); better to
#		stay away from using names such these to avoid collisions with future changes
#
#	* single underscore ['_']
#		- sometimes used as name to indicate that a variable is temporary or insignificant
#		- useful in tuple unpacking (destructuring) to ignore certain fields
#
print("----------------------- underscores -----------------------")

print()
test = Test()
print(test.foo)
print(test._bar)
print(test.def_)
# print(test.__dun) # this line raises a AttributeError ('Test' has no attribute '__dun')
# print(test._Test__dun)
test.count_to_five()
