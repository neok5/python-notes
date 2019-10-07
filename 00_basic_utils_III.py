# DEL keyword | syntax: 'del obj_name'
#
#	It could be used with variables, objects, lists, items within lists, dicts, etc.
#	Below there are several examples
#
print("----------------------- 'del' keyword -----------------------")

class ClassToRemove:
	pass

print(f"Object type -> {type(ClassToRemove)}")
print('Deleting user-defined object.......................')
del ClassToRemove
# print(type(ClassToRemove)) # throws a 'NameError' (name 'ClassToRemove' is not defined)
print()

my_var = 23
my_tuple = ('Goku', 9000)
my_list = ["a", "b", "c"]
my_dict = { 'name' : 'Alberto', 'age' : 27 }
print(f"""var = {my_var}
tuple = {my_tuple}
list = {my_list}
dict = {my_dict}""")
print('Deleting vars, tuples, lists and dicts.......................')
del my_var
del my_tuple # but you can't remove a tuple element; tuples are inmutable
del my_list
del my_dict
# print(my_var); print(my_tuple); print(my_list); print(my_dict) # throws a 'NameError'
print()

_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Original list -> {_list}')
del _list[4] # remove fifth element
print(f'After remove fifth element -> {_list}')
del _list[0:2] # remove first two items
print(f'After remove first two items -> {_list}')
del _list[:] # remove all elements (empty list)
print(f'After remove remain elements -> {_list}')
del _list # remove the list itself, the variable
# print(_list) # throws a 'NameError', as expected
print()

_dict = { 'key_one': 'value_one', 'key_two': 'value_two', 'key_three': 'value_three' }
print(f'Original dict -> {_dict}')
del _dict['key_two'] # remove second dictionary entry (key-value par)
print(f'After remove second entry -> {_dict}')
print()