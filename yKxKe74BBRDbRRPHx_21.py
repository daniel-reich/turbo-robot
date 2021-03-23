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
    def __init__(self, number):
        self.number = number
        
    def __int__(self):
        return(int(self.number))
​
    def __float__(self):
        return(float(self.number))
​
    def __str__(self):
        return(str(self.number))
​
    def __repr__(self):
        return("Number(%s)"%str(self.number))
​
    def __add__(self, other):
        if isinstance(other, Number):
            return(Number(self.number + other.number))
        return(Number(self.number + other))
​
    def __radd__(self, other):
        return(Number(self.number + other))
​
    def __sub__(self, other):
        if isinstance(other, Number):
            return(Number(self.number - other.number))
        return(Number(self.number - other))
​
    def __rsub__(self, other):
        return(Number(other - self.number))
​
    def __mul__(self, other):
        if isinstance(other, Number):
            return(Number(self.number * other.number))
        return(Number(self.number * other))
​
    def __rmul__(self, other):
        return(Number(self.number * other))
​
    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.number != 0:
                return(Number(self.number / other.number))
            return("ZeroDivisionError")
        if other != 0:
            return(Number(self.number / other))
        return("ZeroDivisionError")
​
    def __floordiv__(self, other):
        if isinstance(other, Number):
            return(Number(self.number // other.number))
        return(Number(self.number // other))
​
    def __eq__(self, other):
        if isinstance(other, Number):
            return(Number(self.number == other.number))
        return(Number(self.number == other))
    
    def __ne__(self, other):
        if isinstance(other, Number):
            return(Number(self.number != other.number))
        return(Number(self.number != other))  
​
    def __ge__(self, other):
        if isinstance(other, Number):
            return(Number(self.number > other.number))
        return(Number(self.number > other))
​
    def __gt__(self, other):
        if isinstance(other, Number):
            return(Number(self.number >= other.number))
        return(Number(self.number >= other))

