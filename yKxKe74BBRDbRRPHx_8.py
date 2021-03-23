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
  def __init__(self, value):
    self.number = Number.__val__(value)
    
  def __val__(value):
    return value.number if isinstance(value, Number) else value
​
  def __add__(self, value):
    return Number(self.number + Number.__val__(value))
    
  def __sub__(self, value):
    return Number(self.number - Number.__val__(value))
    
  def __mul__(self, value):
    return Number(self.number * Number.__val__(value))
​
  def __radd__(self, value):
    return value + self.number
    
  def __rsub__(self, value):
    return value - self.number
    
  def __rmul__(self, value):
    return value * self.number
    
  def __truediv__(self, value):
    v = Number.__val__(value)
    if v == 0: return 'ZeroDivisionError'
    return Number(self.number / v)
    
  def __floordiv__(self, value):
    v = Number.__val__(value)
    if v == 0: return 'ZeroDivisionError'
    return int(self.number // v)
​
  def __int__(self):
    return int(self.number)
​
  def __str__(self):
    return str(self.number)
​
  def __eq__(self, other):
    return self.number == other.number if isinstance(other, Number) else False
​
  def __lt__(self, other):
    return self.number < other.number if isinstance(other, Number) else False
​
  def __le__(self, other):
    return self.number <= other.number if isinstance(other, Number) else False
​
  def __gt__(self, other):
    return self.number > other.number if isinstance(other, Number) else False
​
  def __ge__(self, other):
    return self.number >= other.number if isinstance(other, Number) else False
​
obj2 = Number(5)

