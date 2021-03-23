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
​
    def __init__(self, data):
        self.data = data
​
    def __add__(self, other):
        return (Number(self.data + other.data) if type(other) == Number else
                Number(self.data + other))
​
    def __sub__(self, other):
        return (Number(self.data - other.data) if type(other) == Number else
                Number(self.data - other))
​
    def __mul__(self, other):
        return (Number(self.data * other.data) if type(other) == Number else
                Number(self.data * other))
​
    def __truediv__(self, other):
        try:
            return (Number(self.data / other.data) if type(other) == Number else
                    Number(self.data / other))
        except ZeroDivisionError:
            return 'ZeroDivisionError'
​
    def __int__(self):
        return int(self.data)
​
    def __float__(self):
        return float(self.data)
​
    def __eq__(self, other):
        return self.data == other.data
​
    def __str__(self):
        return str(self.data)

