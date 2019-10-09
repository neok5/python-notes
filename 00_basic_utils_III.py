# DEL keyword | syntax: 'del obj_name'
#
#	It could be used with variables, objects, lists, items within lists, dicts, etc.
#	Below there are several examples
#
import math
import random as rnd

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

# TRUNCATE numbers (floats) - using math.trunc(num) function, that returns integer part of 'num'
print("----------------------- truncate numbers -----------------------")

number = 23.3427532
print(f'Original value {number}')
print(f'Integer part: {math.trunc(number)}')  # truncates without rounding the number, just cutting it off

n_decimals = 3
stepper = 10.0 ** n_decimals
print(f'Truncated (3-decimal) value {math.trunc(stepper * number) / stepper}')
print()

# using 'random' module - it allows to generate random numbers
print("----------------------- randomness -----------------------")
print(f'Float random number: {rnd.random()}')
print(f'Float random number in range [2, 7): {rnd.uniform(2, 7)}')
print(f'Integer random in range [70, 100): {rnd.randrange(70, 100)}')  # start is optional (defaults 0)
print(f'Integer pair random in range [0, 11): {rnd.randrange(0, 11, 2)}')  # third argument is the 'step'

num_list = [1, 2, 3, 4, 5]
word = 'spectacular'
print(f'\nNumbers list: {num_list} | Random number choice: \'{rnd.choice(num_list)}\'')
print(f'Word: {word} | Random letter choice: \'{rnd.choice(word)}\'')
rnd.shuffle(num_list)
print(f'Unordered number list: {num_list}')
print(f'Single sample from numbers: {rnd.sample(num_list, 1)}')
print(f'Single sample from word: {rnd.sample(word, 1)}')
print(f'Three letters from word: {rnd.sample(word, 3)}')
print()