my_tuple = ("Goku", 23, 5, 1992, "Goku") # declaration and definition
# you can declare it without params, like: my_tuple = "Goku", 23, 5, 1992, "Goku"

tuples_tuple = ((1, 2), 3) # you can have lists of lists
print(tuples_tuple)
print()

print(my_tuple) # access all elements
print(my_tuple[1]) # access second element
print()

# unlike lists, tuples are inmutable, you can't add or remove elements
# my_tuple.append("extra_element") # this would be wrong

print(1992 in my_tuple) # return if the element is in the tuple
print()

print(my_tuple.index(1992)) # returns the index of the specified element; could raise a ValueError (element not in tuple)
print()

print(my_tuple.count("Goku")) # return the number of times it contains the element
print()

single_element = (2) # just an integer; one element
print(single_element)
# print(len(single_element)) this would lead to failure; cannot len() over a integer
single_element = ("singleton")
print(single_element)
print(len(single_element)) # but in this case, python see the element as a character array (list)
print()

unitary_tuple = ("singleton",) # unitary tuple, with only one element
print(unitary_tuple)
print(len(unitary_tuple))
print()

varied_tuple = ("cero", 1, "2") # tuple unpackage (destructuring)
cero, one, two = varied_tuple
print(cero, one, two)