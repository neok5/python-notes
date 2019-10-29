#
# DECORATORS
#
#	Wrappers for functions or classes, that could be used to modify input-output values, or even modify
#	the function/class itself, before it gets executed. Their basic structure is composed by 3 functions (A, B and C)
#	where A receives B and returns another function C. A decorator always returns a function.
#
#			def A(B):								|	def decorator(function):
#				def C():							|		def internal():
#					# C implementation using B		|			# 'internal' implementation using 'function'
#				return C							|		return internal
#
from functools import wraps, lru_cache as cache
from datetime import datetime as dt


def log_decorator(function):
    def apply_log():
        print('\tCalculating result...', end=' ')
        print(function())
        print('\tCalculation done.')
        print()

    return apply_log


def log_decorator_w_params_and_keyword_params(function):
    # with '*' it receives all arguments regardless how many they are
    # using '**' is the same for keywords params
    def apply_log(*args, **kwargs):
        print('\tCalculating result...', end=' ')
        print(function(*args, **kwargs))
        print('\tCalculation done.')

    return apply_log


@log_decorator
def _sum():
    return 23 + 5


@log_decorator
def _sub():
    return 32 - 5


@log_decorator_w_params_and_keyword_params
def _pow(base, exponent):
    return pow(base, exponent)


print("---------------------- Decorating calculations (basic) -----------------------\n")

_sum()
_sub()

print("---------------------- Decorating calculations (advanced) -----------------------\n")

keyword_params = {'exponent': 10, 'base': 2}
_pow(**keyword_params)
print()

#
#	To decorate a 'function' with a 'decorator' we have to ANNOTATE it with the annotation '@decorator_name'.
#	When we decorate a function with another one, we're replacing function declaration with decorator declaration,
#	so we might want to use @wraps annotation, to preserve those values. Wraps (f - function, d - decorator):
#		a) copies [__module__, __name__, __qualname__, __doc__, __annotations__] attributes from 'f' to 'd'
#		b) updates d.__dict__ with all elements from f.__dict__
#		c) sets a new '__wrapped__ = f' attribute on 'd'
#
print("---------------------- Decorating with 'wraps' -----------------------\n")


def debug(f_):
    @wraps(f_)
    def wrapper(*args, **kwargs):
        """Docstring wrapper"""
        output = f_(*args, **kwargs)
        print(f'\n\t{f_.__doc__}')  # without @wraps, f_.__doc__ would be "Docstring wrapper", instead of "Docstring f"
        print(f'\t{f_.__name__}({args}, {kwargs}) -> {output}')
        print('\n\tCalling "d" function')
        return output

    return wrapper


@debug
def f():
    """Docstring f"""
    print('\tCalled "f" function')


f()
print()
print(f'\tf docstring -> {f.__doc__}')
print(f'\twrapper docstring -> {f.__wrapped__.__doc__}')  # with @wraps, __wrapped__ == f
print()

#
#	Using decorators, we can apply MEMOIZATION: capacity to make a function able to remember values from previous
#	executions so it saves time and resources. The main idea is to wrap a function with a CACHE mechanism, without
#	modify the logic of the function. We can also use @lru_cache annotation to achieve the same goal.
#
print("---------------------- Applying memoization to fibonacci -----------------------\n")


def fibo(n):
    return n if n < 2 else fibo(n - 1) + fibo(n - 2)


def memoize(fun):  # memoize decorator
    fun.cache = dict()

    @wraps(fun)
    def _memoize(*args):
        if args not in fun.cache:
            fun.cache[args] = fun(*args)
        return fun.cache[args]

    return _memoize


@memoize
def memoize_fibo(n):
    return n if n < 2 else memoize_fibo(n - 1) + memoize_fibo(n - 2)


# we only need to remember 3 values: n, n-1 and n-2
@cache(maxsize=3)  # less than 3 is exponentially more time, with few less memory usage
def cached_fibo(n):
    return n if n < 2 else cached_fibo(n - 1) + cached_fibo(n - 2)


init_time = dt.now()
print(f'\t30th fibonacci number: {fibo(30)}')
end_time = dt.now()
time_spent = end_time - init_time
print(f'\tTime spent: {time_spent.seconds}.{time_spent.microseconds} sec')

init_time = dt.now()
print(f'\n\t230th cached fibonacci number: {memoize_fibo(230)}')
end_time = dt.now()
time_spent = end_time - init_time
print(f'\tTime spent: {time_spent.seconds}.{time_spent.microseconds} sec')

init_time = dt.now()
print(f'\n\t400th cached fibonacci number: {cached_fibo(400)}')
end_time = dt.now()
time_spent = end_time - init_time
print(f'\tTime spent: {time_spent.seconds}.{time_spent.microseconds} sec')
print()

#
#	We can have decorators for CLASSES and their INSTANCE METHODS, CLASS METHODS and STATIC METHODS.
#	We have to take into account the kind of method it is to be able to manipulate its parameters properly.
#
print("---------------------- Singleton, instance/class/static methods  -----------------------\n")


def singleton(cls):
    instances = dict()

    @wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Unique:
    def __init__(self):  # executed just once
        print('\tExecuting init')


unique1 = Unique()
unique2 = Unique()  # second call just returns the single instance, does NOT create a new one
unique1.added_value = 23
unique2.added_value = 32

print(f'\tAdded value from unique1: {unique1.added_value}')
print(f'\tAdded value from unique2: {unique2.added_value}')


def instancemethod_decorator(fun):
    @wraps(fun)
    def internal_function(self, *args, **kwargs):  # watch out with received extra number of params: self
        fun(self, *args, **kwargs)

    return internal_function


def classmethod_decorator(fun):
    @wraps(fun)
    def internal_function(cls, *args, **kwargs):  # watch out with received extra number of params: cls
        fun(cls, *args, **kwargs)

    return internal_function


def staticmethod_decorator(fun):
    @wraps(fun)
    def internal_function(*args, **kwargs):  # watch out with received extra number of params: None
        fun(*args, **kwargs)

    return internal_function


class Foo:
    @instancemethod_decorator
    def instancemethod(self, *args, **kwargs):
        print(f'\t\tself: {self} | args: {args} | kwargs: {kwargs}')

    @classmethod
    @classmethod_decorator
    def classmethod(cls, *args, **kwargs):
        print(f'\t\tcls: {cls} | args: {args} | kwargs: {kwargs}')

    @staticmethod
    @staticmethod_decorator
    def staticmethod(*args, **kwargs):
        print(f'\t\targs: {args} | kwargs: {kwargs}')


foo = Foo()

print(f'\n\tInstance methods:')
foo.instancemethod(1, 2, a=3, b=4)  # CAREFUL with this
Foo.instancemethod(1, 2, a=3, b=4)  # instance methods expect 'self' as first value, but Foo hasn't got it

print(f'\n\tClass methods:')
foo.classmethod(1, 2, a=3, b=4)
Foo.classmethod(1, 2, a=3, b=4)

print(f'\n\tStatic methods:')
foo.staticmethod(1, 2, a=3, b=4)
Foo.staticmethod(1, 2, a=3, b=4)
