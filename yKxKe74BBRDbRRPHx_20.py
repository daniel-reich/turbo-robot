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
    self.v = val
  
  def __add__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v + other)
    else:
      return Number(self.v + other.v)
  
  def __sub__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v - other)
    else:
      return Number(self.v - other.v)
  
  def __rsub__(self, other):
    return Number(other - self.v)
  
  def __mul__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v * other)
    else:
      return Number(self.v * other.v)
  
  def __rmul__(self, other):
    print(self, other)
    return Number(self.v * other)
  
  def __truediv__(self, other):
    if other == 0 or other.v == 0:
      return 'ZeroDivisionError'
    if isinstance(other,int) == True:
      return Number(self.v / other)
    else:
      return Number(self.v/other.v)
  
  def __floordiv__(self, other):
    if other == 0 or other.v == 0:
      return 'ZeroDivisionError'
    if isinstance(other, int) == True:
      return Number(self.v//other)
    else:
      return Number(self.v//other.v)
  
  def __str__(self):
    return str(self.v)
  
  def __int__(self):
    return int(self.v)
  
  def __repr__(self):
    return 'Number({})'.format(self.v)
  
  def __float__(self):
    return float(self.v)
  
  def __eq__(self, other):
    print(self, other)
    if isinstance(other, int) == True:
      return self.v == other
    return self.v == other.v
  
  def __gt__(self, other):
    if isinstance(other, int) == True:
      return self.v > other
    return self.v > other.v
  
  def __ge__(self, other):
    if isinstance(other, int) == True:
      return self.v >= other
    return self.v >= other.v
  
  def __lt__(self, other):
    if isinstance(other, int) == True:
      return self.v < other
    return self.v < other.v
  
  def __le__(self, other):
    if isinstance(other, int) == True:
      return self.v <= other
    return self.v <= other.v

