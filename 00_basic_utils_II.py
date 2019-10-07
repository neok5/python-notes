import math as ma

# function print() with param keywords
#	'sep' - printed elements separator; default value: ' '
# 	'end' - indicates the 'str' printed at last; default value: '\n'
#		useful when you want to avoid the line feed ('\n') of print()
#	'file' - object with write(string) method; default value: 'sys.stdout'
#		it could be an opened file to write in it
print("----------------------- print() with leywords -----------------------\n")
print("word one", "word two", "word three", sep = '')
print("word one", "word two", "word three", sep = ' | ')
print("word one", "word two", "word three", sep = '\t')
print("word1", end = '') # removes the line feed
print("\n") # used with '\n' to compensate line just above

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
#	except CaugthException as e:
#		error_handling # here 'e' can be used as the exception variable
#	finally:
#		opened_file.close()
print("----------------------- 'with' and 'pass' -----------------------\n")
try:
	with open('file_path', 'r') as opened_file:
		data = opened_file.read() # it closes the resource itself
except FileNotFoundError as e:
	print(f"Exception raised:\n\t{e}")

# PASS statement | is a null operation; when is executed, nothing happens
# useful as placeholder when a statement is required syntactically
class ClassNotImplementedYet:
	pass

	def function_not_implemented_yet(self):
		pass
print()

# UNDERSCORES | they have 5 principal uses or patterns:
#
#	* single leading underscore ['_var']
#		- by convention, indicates the element isn't intended to be externally accessed
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
#		- stay away from using names such these to avoid collisions with future changes
#
#	* single underscore ['_']
#		- sometimes used as name to indicate that a variable is temporary or insignificant
#		- useful in tuple unpacking (destructuring) to ignore certain fields
#
print("----------------------- underscores -----------------------\n")

class Test:
	def __init__(self):
		self.foo = 'foo'
		self._bar = '_bar'
		self.def_ = 'def_' # use 'self.def' raises a SyntaxError, as 'def' is a keyword
		self.__dun = '__dun' # name mangling converts '__dun' to '_Test__dun'

	def count_to_five(self):
		for _ in range(1,6): # '_' use as temporary varname
			print(_, end = "\n" if _ == 5 else " ")

test = Test()
print(test.foo)
print(test._bar)
print(test.def_)
# print(test.__dun) # this line raises a AttributeError ('Test' has no attribute '__dun')
# print(test._Test__dun)
test.count_to_five()
print()

# shorter FOR; syntax: we can apply 'map' and 'filter' to a list with a shorten FOR
# 	'[function(ele) for ele in elements if condition(ele)]'
# 	'[map_function shorten_FOR if filter_function]'
print("--------------- shorter FOR [map(), filter() combination] ---------------\n")
numbers = [0, 1, 2, 4, 9, 16, 25, 36, 50] # 9 numbers, 7 integer sqrts (not '2' and '50')
square_roots = [ ma.sqrt(n) for n in numbers if ma.modf(ma.sqrt(n))[0] == 0]
print(square_roots) # prints only integer square roots (decimal part = 0)
print()