#
#   FUNCTIONAL PROGRAMMING
#
#       It's a programming paradigm characterized by the use of mathematical functions, where functions
#       have no side effects, and function's result just depends on the input parameters.
#
#   RECURSION
#
#       In functional paradigm it's not usually the use of iterations, but recursion it's very common instead.
#       A recursive function has a recursive case, while the functions keeps calling itself with different inputs,
#           and a base case, which represents the stop condition for the function, and the return of the result.
#       A recursive function's flow would be as follows: first, the functions starts to call itself repeatedly,
#           providing different arguments for each call, in a descendant process, and second (and lastly), the function
#           starts from bottom to top, to use these input params to do some kind of calculus, returning each partial
#           result of the calculus in an ascendant process, combining the results at the same time with a final output.
#
#   REDUCE FUNCTION
#
#       Considered as high order function.
#       Applies a function to each par of elements in an iterable, storing the result of each operation, and combining
#       it with the subsequent element, finally returning the complete result of function partial applications.
#
#   CLOSURES
#
#       A nested function is the one that is defined within another main function. Nested functions can access
#           to variables of main function scope (readonly by default in Python).
#       A closure it's a function object that remembers (stores) the values of variables in included scopes,
#           even if they're not in memory anymore.
#
#   COMPREHENSIONS
#
#       Collection/container comprehensions. Generates collections/containers from iterables, allowing to add
#       optional conditionals in the process. These collections could be lists, tuples (create generators),
#       sets, dicts... Syntax:
#                               [|(|{ "map_function" for element in iterable if "filter_function" }|)|]
#
from functools import reduce, partial

print("\n---------------------- Recursion -----------------------")
def recursive_factorial(num):
    return 1 if num == 1 or num == 0 else num * recursive_factorial(num-1)

print(f'\n\tFactorial of 5 -> {recursive_factorial(5)}')

print("\n---------------------- Reduce function -----------------------\n")
def reduce_factorial(num):
    # 1 as initial value prevents errors, and it's useful as default value for 0 or smaller numbers
    return reduce(lambda x, y: x*y, range(1, num+1), 1)

print(f'\tFactorial of -5 -> {reduce_factorial(-5)}')
print(f'\tFactorial of 5 -> {reduce_factorial(5)}')
print(f'\tFactorial of 0 -> {reduce_factorial(0)}')

print("\n---------------------- Closures -----------------------")
def build_n_times_multiplier(n):
    def multiply_n_times(m):
        return n*m
    return multiply_n_times

multiplier_by_3 = build_n_times_multiplier(3)
print(f'\n\t3 times 5 -> {multiplier_by_3(5)}')
print(f'\t3 times 23 -> {multiplier_by_3(23)}')
multiplier_by_5 = build_n_times_multiplier(5)
print(f'\t5 times 0 -> {multiplier_by_5(0)}')
print(f'\t5 times -2 -> {multiplier_by_5(-2)}')


print("\n---------------------- Partials -----------------------")
def sum_(x, y):
    return x + y

plus_two = partial(sum_, 2)
print(f'\n\t10 plus 2: {plus_two(10)}')
print(f'\t-2 plus 2: {plus_two(-2)}')
pair_number_filter = partial(lambda x, y: x % y, y=2)
print(f'\t23 is a pair number? {pair_number_filter(23) == 0}')
print(f'\t32 is a pair number? {pair_number_filter(32) == 0}')

print("\n---------------------- Comprehensions -----------------------")
squares_list = [n ** 2 for n in range(1, 11)]
print(f'\n\tList of squares from 1 to 10 -> {squares_list}')
pair_squares_list = [n ** 2 for n in range(1, 11) if n % 2]
print(f'\tList of pair squares from 1 to 10 -> {pair_squares_list}')

squares_tuple = (n ** 2 for n in range(1, 11))
print(f'\n\tTuple of squares from 1 to 10 -> {squares_tuple}')
pair_squares_tuple = (n ** 2 for n in range(1, 11) if n % 2)
print(f'\tTuple of pair squares from 1 to 10 -> {pair_squares_tuple}')

squares_set = {n ** 2 for n in range(1, 11)}
print(f'\n\tSet of squares from 1 to 10 -> {squares_set}')
pair_squares_set = {n ** 2 for n in range(1, 11) if n % 2}
print(f'\tSet of pair squares from 1 to 10 -> {pair_squares_set}')

squares_dict = {n: n ** 2 for n in range(1, 11)}
print(f'\n\tDict of squares from 1 to 10 -> {squares_dict}')
pair_squares_dict = {n: n ** 2 for n in range(1, 11) if n % 2}
print(f'\tDict of pair squares from 1 to 10 -> {pair_squares_dict}')
