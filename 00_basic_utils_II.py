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
my_dict = {'name': 'Alberto', 'age': 27}
print(f"""var = {my_var}
tuple = {my_tuple}
list = {my_list}
dict = {my_dict}""")
print('Deleting vars, tuples, lists and dicts.......................')
del my_var
del my_tuple  # but you can't remove a tuple element; tuples are immutable
del my_list
del my_dict
# print(my_var); print(my_tuple); print(my_list); print(my_dict) # throws a 'NameError'
print()

_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Original list -> {_list}')
del _list[4]  # remove fifth element
print(f'After remove fifth element -> {_list}')
del _list[0:2]  # remove first two items
print(f'After remove first two items -> {_list}')
del _list[:]  # remove all elements (empty list)
print(f'After remove remain elements -> {_list}')
del _list  # remove the list itself, the variable
# print(_list) # throws a 'NameError', as expected
print()

_dict = {'key_one': 'value_one', 'key_two': 'value_two', 'key_three': 'value_three'}
print(f'Original dict -> {_dict}')
del _dict['key_two']  # remove second dictionary entry (key-value par)
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

# DOCSTRINGS - documentation of modules, classes, functions, etc.
# ANNOTATIONS - they can be used to help to identify expected values as parameters of a function
class Dummy:
    """Dummy documentation about Dummy class"""
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __str__(self):
        return f'{self.param_1}-----{self.param_2}'

def example_function(num_1: int, chars: str, days: list) -> Dummy:  # we specify param types and return type
    return Dummy(f'{str(num_1)}{chars}', days)


print(Dummy.__doc__)
print(example_function(23, '_test', ['monday', 'friday', 'thursday']))

# CONTEXT MANAGERS - they allow to build code with pre and post conditions, executing actions before and after
#					 the actual (main) code runs. They consist of two magic methods: __enter__ and __exit__
def start_db():
    pass  # code to start the db

def stop_db():
    pass  # code to stop the db

class DBHandler:
    def __enter__(self):
        """Executed before db_backup static method"""
        start_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Executed after db_backup static method"""
        stop_db()

    @staticmethod
    def db_backup():
        """Main code in the class"""
        pass  # code to make a db backup

with DBHandler():
    DBHandler.db_backup()

# SUBPROCESS MODULE
#
#	- It allows to spawn new processes, connect them to their input/output/error pipes, and obtain their
#       return codes. The recommended approach to invoking subprocess is to use the run() function for
#       all use cases it can handle. For advanced use cases, Popen interface can be used.
#
#   - Function subprocesss.run. Run the command described by args, wait for it to complete and then
#       return a CompletedProcess instance, representing a process that has finished, which contains:
#           · 'args', the args used to launch the process
#           · 'returncode', the exit status of the child process, where 0 indicates success, and a negative
#                           value indicates a signal of termination (POSIX only)
#           · 'stdout' | 'stderr', from the child process. None if not captured, a byte sequence by
#                                  default, or a string if run() was called with 'universal_newlines=True'
#
#   - Function subprocess.Popen. Execute a child program in a new process. It's the underlying layer of
#       run() function, so this last is just a wrapper over Popen, in order to simplify its use.
#

#
# MONKEY PATCH/PATCHING - It's simply the dynamic replacement of attributes at runtime
#

#
# SET operations: intersection, union, symmetric difference, difference, superset...
#
spam = set('spam')
eggs = set('eggs')

print()
print(spam, eggs, sep='\n', end='\n\n')

print(f'spam & eggs: {spam & eggs}')  # AND - intersection (all letters in both words)
print(f'spam | eggs: {spam | eggs}')  # OR - union (all letters in both words)
print(f'spam ^ eggs: {spam ^ eggs}')  # XOR - symmetric difference (all letters in both words, except common ones)
print(f'spam - eggs: {spam - eggs}')  # NOT IN - difference (all letters in first word, not in the second one)
print(f'eggs - spam: {eggs - spam}')
print(f'spam > eggs: {spam > eggs}')  # ALL IN - superset(true if first word contains,
print(f'eggs > spam: {eggs > spam}')  # at least, all letters of second word; false otherwise)
print(f'perfection > perfect: {set("perfection") > set("perfect")}')

#
#   USE of 'if __name__ == "__main__"' in a MODULE
#       When Python interpreter reads a source file it does two things:
#           - It sets some special variables, such '__name__', and then
#           - executes all the code found in the file, sentence by sentence
#       A module (python file) can be used in two ways:
#           - It gets executed directly. It's the main program: __name__ == "__main__"
#           - It gets imported w/ or wout/ an alias. It's NOT the main program: __name__ == "module_name_used_to_import"
#
