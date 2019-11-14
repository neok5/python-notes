#
# LAMBDA FUNCTIONS
#
#	- They are like anonymous functions, syntactic sugar that Python adds to shorten
#	  the code; it just consist in sum up a normal function into a lambda function
#
#	- All you can do with a lambda function can be done with a normal function,
#	  but it doesn't work in reverse, not all you can do with a normal function can
#	  be done using lambda functions. For example, a lambda function can't have
#	  flow control statements such as conditional structures or loops
#
#	- Syntax:
#				lambda [input_arguments]: [result_expression]
#
print("----------------------- Lambda functions examples ------------------------\n")

def triangle_area(base, height):
    return base * height / 2

print(f'\t[NORMAL] The area of a triangle (3 base, 5 height) is {triangle_area(3, 5)}')
print()

#triangle_area_lambda = lambda b, h: b * h / 2  # do not assign a lambda expression, use a def
#print(f'\t[LAMBDA] The area of a triangle (3 base, 5 height) is {triangle_area_lambda(3, 5)}')
print(f'\t[LAMBDA] The area of a triangle (3 base, 5 height) is {(lambda b, h: b * h / 2)(3, 5)}')
print()

#
# FILTER FUNCTION
#
#	- Considered as high order function
#
#	- Checks which elements in a collection meets a condition and returns an iterator 
#	  with the elements that satisfy that condition; i.e.: filters the collection
#
print("----------------------- Filtering pair numbers ------------------------\n")

numbers = [17, 24, 7, 39, 8, 51, 92, 23, 32]

def pair_numbers_filter(num):
    return num % 2 == 0

print(f'\tOriginal list -> {numbers}')
print(f'''
    Filtered list using normal function -> {list(filter(pair_numbers_filter, numbers))}''')
print(f'''
    Filtered list using lambda function -> {list(filter(lambda n: n % 2 == 0, numbers))}''')
print()

print("----------------------- Filtering employees ------------------------\n")

def show_employees(employees_):
    for emp in employees_:
        print(f'\t\t· {emp}')

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'{self.name} works as {self.position} with a salary of {self.salary} $/year'

employees = [Employee('Isaac', 'professor', 42000),
             Employee('Leonardo', 'wise man', 500000),
             Employee('Albert', 'visionary', 230000),
             Employee('Stephen', 'theoretical physicist', 95000),
             Employee('Will', 'wild man', 0), ]

print('\tEmployee list:\n')
show_employees(employees)
print(f'\n\tRich employees:\n')
show_employees(filter(lambda e: e.salary > 92000, employees))
print()

#
# MAP FUNCTION
#
#	- Considered as high order function
#
#	- Applies a specified function to each element of an iterable (list, tuple, etc.),
#	  and return ANOTHER list with the results after apply the function
#
#   - It returns a map object, which is lazy evaluated, so each result of the function over the iterable element,
#     it's calculated on demand when it's required, in subsequent callings to the iterable.
#
print("----------------------- Mapping employees salaries ------------------------\n")

def increment_by_10_percent(employee):
    employee.salary = employee.salary * 1.1 // 1  # to shorten the precision
    return employee

print(f'\tOriginal list of employees:\n')
show_employees(employees)
print(f'\n\tMapped list with salaries below 100.000 $/year increased by 10% more:\n')
show_employees(map(increment_by_10_percent, filter(lambda e: e.salary < 100000, employees)))
print()
