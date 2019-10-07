my_list = ["uno", 2, "3"] # declaration and definition
print(my_list)

complex_list = [[1, 2], 3] # you can have lists of lists
print(complex_list) # access all elements; same as 'print(my_list[:])'

print(my_list[0]) # access first element; could raise an IndexError (out of list limits)
print(my_list[-2]) # same, accessing with reverse index

print(my_list[0:1]) # list portion; example = only first element
					# left: inclusive (default: 0), right: exclusive (default: list_size)

# we can also use list's portions to delete list fragments
my_list[:2] = [] # deleting first two elements
print(my_list)
my_list.insert(0, 2)
my_list.insert(0, 'uno')

my_list.append("4th") # insert one element at the end
print(my_list)

my_list.insert(0, "0") # insert one element at specified index
print(my_list)

my_list.extend(["cinco", "SIX"]) # concat another list at the end
print(my_list)

print(my_list.index("4th")) # returns the index of the specified element; could raise a ValueError (element not in list)

print("4th" in my_list)  # return if the list contains the element

my_list.remove("uno") # delete the specified element
print(my_list)

my_list.pop() # delete the last element of the list
print(my_list)

list_1 = [3, 23.5, "último"]
list_2 = ["+-*/", 5, "last"]
print(list_1 + list_2) # concat both lists

# we can reverse a list two ways: the first one modify the original list, the second one returns a copy
my_list.reverse() # using 'reverse' list function
print(my_list)
my_list = my_list[::-1] # using a third index for list portion, indicating reverse way for build output list
print(my_list)

list_simple = ["A"]
print(list_simple)

list_triple = list_simple * 3
print(list_triple) # multiplies the list, concatening it N times