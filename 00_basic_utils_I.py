# function len() | return the number of elements of the iterable
#				   it works if the iterable is a string (char list)
print("----------------------- len() -----------------------")
print(len(range(0,2)))
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
import math
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
print(f"Thrird element: {str(next(my_iterator))}")
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
for n in returned_numbers: # first 'next' element (1)(3)(5); excluded values
	# second 'next' element (2)(4)('\n'); printed values
	print(next(returned_numbers, "\n"), end = " ")
print() # the loop fetch 2 values of generator per iteration

# you can also use a list as actual params in a function call
# this way, the '*' operator spreads the list and the function
# receives the params as separated arguments instead of a list
print("----------------------- * as actual params prefix -----------------------")
print(list(range(3, 6)))            # normal call with separate arguments = [3, 4, 5]
args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list = [3, 4, 5]
print()

# KEYWORD PARAMS (arguments passed using its formal param name)
# you can also declare formal params with '**' when they are keyword ones
print("----------------------- ** as formal and actual params prefix -----------------------")
def local_pow(base, exponent):
	return pow(base, exponent)

def _pow(*args, **kwargs):
	return local_pow(*args, **kwargs)

print(f'\tPow with ordered params: {_pow(2, 10)}')
keyword_arguments = { 'exponent' : 10, 'base' : 2 }
print(f'\tPow with unordered params (using keywords): {_pow(**keyword_arguments)}\n')