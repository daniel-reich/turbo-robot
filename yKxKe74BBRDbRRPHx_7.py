"""


Most people don't know about magic methods, which is sad, because they are
incredibly powerful and are used in built-in functions such as `int()`,
`print()`, `repr()`, and even iteration and indexing.

Use magic methods (don't forget `__init__`) to create a `Number` class.

### Examples

    __int__     # Used in the "int" method
    __float__   # Used in the "float" method
    __str__     # Used in the "str" method
    __repr__    # Used in the "repr" method
    __add__     # Used in the "+" operator function
    __sub__     # Used in the "-" operator function
    __mul__     # Used in the `*` operator function
    __truediv__ # Used in the "/" operator function
    __floordiv__# Used in the "//" operator function

### Notes

N/A

"""

class Number:
    def __init__(self, num):
        self.num = num
    
    def __eq__(self, other):
        if type(other) == Number:
            return self.num == other.num
        return self.num == other
    
    def __float__(self):
        return float(self.num)
    
    def __str__(self):
        return str(self.num)
    
    def __int__(self):
        return int(self.num)
    
    def __add__(self, other):
        if type(other) == Number:
            return Number(self.num + other.num)
        return Number(self.num + other)
    
    __radd__ = __add__
    
    def __mul__(self, other):
        if type(other) == Number:
            return Number(self.num * other.num)
        return Number(self.num * other)
    
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        if other == 0:
            return 'ZeroDivisionError'
        if type(other) == Number:
            return Number(self.num / other.num)
        return Number(self.num / other)
    
    def __rtruediv__(self, other):
        if self == 0:
            return 'ZeroDivisionError'
        try:
            return other / self
        except:
            return Number(other) / self
    
    def __sub__(self, other):
        if type(other) == Number:
            return Number(self.num - other.num)
        return Number(self.num - other)
    
    __rsub__ = lambda self, other: -1 * self + other

