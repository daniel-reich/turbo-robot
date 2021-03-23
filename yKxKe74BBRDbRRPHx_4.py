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
  def __init__(self,num):
    self.value = num
  
  def __eq__(self, other):
    if isinstance(other, Number):
      return self.value == other.value
    return self.value == other
    
  def __ne__(self, other):
    if isinstance(other, Number):
      return self.value != other.value
    return self.value != other
    
  def __gt__(self, other):
    if isinstance(other, Number):
      return self.value > other.value
    return self.value > other
    
  def __le__(self, other):
    if isinstance(other, Number):
      return self.value <= other.value
    return self.value <= other
  
  def __int__(self):
    return int(self.value)
    
  def __float__(self):
    return float(self.value)
    
  def __str__(self):
    return str(self.value)
    
  def __repr__(self):
    return "Number(" + str(self.value) + ")"
    
  def __add__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value + other.value)
  
  __radd__ = __add__
    
  def __sub__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value - other.value)
    
  __rsub__ = __sub__
    
  def __mul__(self,other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value * other.value)
    
  __rmul__ = __mul__
    
  def __truediv__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    if other.value == 0:
      return "ZeroDivisionError"
    return Number(self.value / other.value)
    
  __rtruediv__ = __truediv__
    
  def __floordiv__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    if other.value == 0:
      return "ZeroDivisionError"
    return Number(self.value // other.value)
    
  __rfloordiv__ = __floordiv__
  
  
​
obj2 = Number(5)

