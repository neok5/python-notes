#
# PROPERTIES and property() function
#
#   - When we want to make some kind of conversion, calculus or process when accessing an object value, we can
#   use properties for that. For simple value access, it's preferable to declare attributes the common way.
#
#   - Properties allow direct access to object vars, allowing data encapsulation at the same time. They achieve
#   this through direct syntax (obj.var = value | value = obj.var | del obj.var), but with underlying methods
#   which provides ways to handle those accesses, useful for example for logging tasks.
#
#   - The property function allows to create a property value. Syntax: property(fget, fset, fdel, doc),
#   where 'fget' is a function for getting an attribute value. 'fset' is a function for setting an attribute
#   value, fdel is a function for deleting an attribute value, and 'doc' builds a docstring for the attribute.
#
#   - We have also property decorators, for a more succinct syntax, such as @property for getters, @var.setter
#   for setter and @var.deleter for deleters. In this case, we can provide a docstring for the property putting
#   that docstring within @property annotated function.
#
#   - Second form is preferable.
#

class C1:
    def __init__(self):
        self._x = None

    def getx(self):
        print("getter of x called")
        return self._x

    def setx(self, value):
        print("setter of x called")
        self._x = value

    def delx(self):
        print("deleter of x called")
        del self._x

    def __str__(self):
        return self._x if self._x is not None else '<empty>'

    x = property(getx, setx, delx, "I'm the 'x' property.")

print()
c1 = C1()
print(c1)
c1.x = 'foo'  # setter called
print(c1)
foo1 = c1.x  # getter called
print(c1)
del c1.x  # deleter called
print(c1.__repr__())

class C2:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""  # same as 'doc' argument of property function
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x

    def __str__(self):
        return self._x if self._x is not None else '<empty>'

print()
c2 = C2()
print(c2)
c2.x = 'foo'  # setter called
print(c2)
foo2 = c2.x  # getter called
print(c2)
del c2.x  # deleter called
print(c2.__repr__())
