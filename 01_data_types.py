# PYTHON DATATYPES
#
# 1. Numbers
# 		A. int
#		B. float
#		C. complex
#			complex(real_part, [imaginary_part])
#				imaginary_part default value: 0
#
# 2. Strings (str)
#	- a dobule """ can be used to span a str into several lines
#	- they can be accessed as arrays/lists ('[' index ']' notation)
#	- three ways of formatting a str:
#		+ print("I printed %s pages in printer %s" % (x, printer))
#		+ print("I printed {0} pages in printer {1}".format(x, printer)); alternativly:
#		  print("I  printed {x} pages in printer {printer}".format(x=7, printer="Dell"))
#		+ print(f"I just printed {x} pages to the printer {printer}")
#		  	# with 'x' and 'printer' as external vars
#
# 3. Lists, tuples, dictionaries, ranges...
#
# 4. Booleans (bool)
# 	- they can only be 'True' or 'False'
#
# 5. Sets (set)
#	- they doesn't allow repeated values, a={1,2,2,3} is saved as a={1,2,3}
#	- they are unordered, so they doesn't allow index access neither
#	- they are mutable, you can add() or discard()[DOES NOT raise an Exception]/
#		remove()[DOES raise an Exception if not found] elements
#	- we can also use s1.update(s2) to add elements in s2 to s1, or we can use s1.union(s2)
#       to return a third set with elements in s1 and s2, without modifying them
#   - all set logic is available using set functions: s1.isdisjoint(s2), s1.issubset(s2), s1.issuperset(s2),
#       s1.difference(s2) [DON'T modify s1 NOR s2] / s1.difference_update(s2) [DO modify s1, but DON'T s2],
#       s1.intersection(s2) and s1.symetric_differece(s2) [the opposite of intersection]...
var = 1
print(type(var))

var = 1.5
print(type(var))

var = complex(5) # same as 'var = complex(5, 0)'
print(type(var))

var = "prueba" # also with single quotes ' '
print(type(var))

var = []
print(type(var))

var = ()
print(type(var))

var = {}
print(type(var))

var = range(0, 6)
print(type(var))

var = True
print(type(var))

# var = {} builds a 'dict', not a 'set'; a 'set' has to have one value at least
var = { None } # empty 'set'; None is a python keyword that indicates value absence
print(type(var))