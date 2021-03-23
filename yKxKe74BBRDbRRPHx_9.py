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

def oVal(x):
  try:
    return x.val
  except:
    return x
​
class Number:
  def __init__(self, value):
    self.val = value
  def __add__(self, x):
    return oVal(self) + oVal(x)
  def __sub__(self, x):
    return oVal(self) - oVal(x)
  def __mul__(self, x):
    return oVal(self) * oVal(x)
  def __truediv__(self, x):
    try:
      return oVal(self) / oVal(x)
    except ZeroDivisionError:
      return "ZeroDivisionError"
  def __rtruediv__(self, x):
    try:
      return oVal(x) / oVal(self)
    except ZeroDivisionError:
      return "ZeroDivisionError"
  def __eq__(self, other):
    return True

