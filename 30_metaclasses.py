#
#   METACLASSES
#
#       In Python we can use several techniques to MODIFY CLASSES BEFORE CREATE THEM, such as inheritance, mixins,
#       decorators... But there's one more advanced technique: METACLASSES. We can use type() to fetch an object's
#       type, passing the object as argument (type(obj) -> obj_type), but also we can use type() to create quick
#       new classes: type(name, bases, namespace) -> new_class_def.
#
#       Metaclasses are like fabrics that allows to create new classes. We can EXTEND FROM 'type' class to CREATE
#       a METACLASS, and with that metaclass, create new classes easily using its properties. We have to define
#       a '__new__' method (similar to '__init__'), we must use params used with type-new-object-type invocation.
#
#       We can use 'abc' module to define ABSTRACT BASE CLASSES, which allow to create metaclasses and define
#       abstract methods for them. With this we can achieve that every subclass of a 'metaclass' class must
#       implement its abstract methods, in a mandatory way, or the subclass invocation will fail.
#       As good examples of intensive use of metaclasses we have 'SQLAlchemy' (Python ORM) and 'Graphene' (GraphQL).
#
from abc import ABCMeta, abstractmethod

print("---------------------- Using type() for new object types -----------------------")
class IntNumber:
    value = 0

DoubleNumber = type('DoubleNumber', (object,), dict(value=0.0))

integer = IntNumber()
double = DoubleNumber()
print(f'\n\tInteger number value -> {integer.value}')
print(f'\tDouble number value -> {double.value}')
print()

print("---------------------- Creating a metaclass -----------------------")

class MetaInteger(type):
    def __new__(mcs, name, bases, namespace):
        name = 'IntegerNumber'  # fixes 'metaclassed' class name
        bases = (int,) + bases  # add int to 'metaclassed' class inheritance classes
        namespace['value'] = 23  # add 'value' class field to 'metaclassed' class fields
        return type.__new__(mcs, name, bases, namespace)  # create and return a new object with specified args

class Number:
    pass

class IntegerNumber(metaclass=MetaInteger):
    pass

print(f'\n\tNumber.__name__: {Number.__name__}')
print(f'\tIs "Number" subclass of "int"? {issubclass(Number, int)}')
#print(f'\tNumber.value: {Number.value}')  # this would throw an AttributeError

print(f'\n\tIntegerNumber.__name__: {IntegerNumber.__name__}')
print(f'\tIs "IntegerNumber" subclass of "int"? {issubclass(IntegerNumber, int)}')
print(f'\tIntegerNumber.value: {IntegerNumber.value}')
print()

print("---------------------- Using 'abc' -----------------------")

class Foo(metaclass=ABCMeta):
    @abstractmethod
    def bar(self):
        raise NotImplemented()

class NewFoo(Foo):
    def new_bar(self):
        pass

#NewFoo()  # this would throw a TypeError (can't instantiate abstract class 'NewFoo' with abstract methods 'bar')

class NewCompletedFoo(Foo):
    def bar(self):
        pass

NewCompletedFoo()  # this WON'T throw an error, because it has its 'bar' superclass abstract method overwritten

print(f'\n\tNewFoo dir() -> {dir(NewFoo)}')  # has 'new_bar' and 'bar'
print(f'\n\tNewCompletedFoo dir() -> {dir(NewCompletedFoo)}')  # has just 'bar'
