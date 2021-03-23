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

def decorator(func):
    def wrapper(*args):
        if isinstance(args[1], Number):
            return func(*args)
        else:
            return func(args[0], Number(args[1]))
    return wrapper
​
class Number:
  def __init__(self, value):
    self.value = value
  
  @decorator
  def __eq__(self, other):
    return self.value == other.value
  
  @decorator
  def __add__(self, other):
    return Number(self.value + other.value)
    
  @decorator  
  def __sub__(self, other):
    return Number(self.value - other.value)
  
  @decorator
  def __mul__(self, other):
    return Number(self.value * other.value)
  
  @decorator
  def __truediv__(self, other):
    if other.value == 0:
      return 'ZeroDivisionError'
    else:
      return Number(self.value / other.value)
  
  def __str__(self):
    return str(self.value)
    
  def __int__(self):
    return int(self.value)
    
  def __float__(self):
    return float(self.value)

