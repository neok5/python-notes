#
# DOCUMENTATION and TEST
#
#	- Documenting is the fact of include comments in the code: classes, methods, modules, etc.
#	  It's useful for workteam, specially in big complex applications.
#
#   - We can also include test in function comments, using 'doctest' Python built-in module.
#     We must import the module, and include the test inside the comment of the function,
#     usually after the description of what the function does. Syntax:
#
#       · >>> function_call([arguments])
#         [expected_result]
#
#     If everything goes fine and all test have success, there will be no output in console.
#     Otherwise, if any test fails, we'll see an error trace with a lot of information.
#
#     We can also use nested expressions for variable building, for example, using ... syntax:
#
#       · >>> _list = []
#         >>> for n in range(5):
#         ...   list.append(element)
#         >>> list_squares(list)
#         [expected_result] # as a list of the squeares of list's elements
#
#   - Instead of print() function, which sends a string provided as param to an output stream
#     (generally the console), we can use help() function, that sends the documentation linked
#     with each code fragment: a class, a method, a module. Therefore, we can print by console
#     the comments contained into such code fragments.
#
#   - Below we have documentation examples of help(), which first line is:
#       'Help on [element] [element_name] in [element_file_relative_route]:'

""" module documentation:

    NAME
        [module_relative_route] - [module_comments]

    CLASSES
        builtins.object
            [class_name]
        [class_documentation_help] # omitted to shorten

    FUNCTIONS
        [functions_documentation_help] # omitted to shorten

    FILE [module_file_absolute_route]
"""

""" class documentation:

    class [class_name](builtins.object)
        [class_name]([constructor_params])
        [class_comments]

        Methods defined here:
        [methods_documentation_help] # omitted to shorten

        Data descriptors defined here:
            __dict__
                dictionary for instance variables (if defined)

            __weakref__
                list of weak references to the object (if defined)
"""

""" function documentation:

    [function_name]([function_params])
        [function_comments]
"""

#import modules.math_functions as ma

#help(ma); help(ma.Number); help(ma.Number.__init__); help(ma.multiply)

import doctest

def number_square(num, text_mode):
    '''returns the square of the provided 'num'

    >>> number_square(2, False)
    4

    >>> number_square(5, True)
    'The result is 25'

    >>> numbers_to_test = []
    >>> for n in range(3,4):
    ...     numbers_to_test.append(n)
    >>> number_square(numbers_to_test[0], False)
    9

    >>> number_square('a', False)
    Traceback (most recent call last):
        ... # 3 dots act as wildcard, so between above and below lines there could be anything
    TypeError: can't multiply sequence by non-int of type 'str'
    '''
    return num*num if not text_mode else f'The result is {num*num}'

doctest.testmod()