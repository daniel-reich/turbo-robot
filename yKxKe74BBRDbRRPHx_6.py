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
    def __init__(self, val):
        self.val = val
​
    def __eq__(self, other):
        return type(self) == type(other) and self.val == other.val
        
    def __str__(self):
        return str(self.val)
​
    def __int__(self):
        return int(self.val)
​
    def __float__(self):
        return float(self.val)
​
    def __add__(self, other):
        return Number(self.val + (other if type(other)==int else other.val))
​
    def __sub__(self, other):
        return Number(self.val - other)
​
    def __mul__(self, other):
        return Number(self.val * (other if type(other)==int else other.val))
​
    def __truediv__(self, other):
        if 0==other:
            return 'ZeroDivisionError'
        return Number(self.val / other.val)

