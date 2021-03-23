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
  def __init__(self, n):
    self.n = n
  def __eq__(self, o):
    if isinstance(o, Number):
      return self.n == o.n
    return self.n == o
  def __ne__(self, o):
    if isinstance(o, Number):
      return self.n != o.n
    return self.n != o
  def __lt__(self, o):
    if isinstance(o, Number):
      return self.n < o.n
    return self.n < o
  def __le__(self, o):
    if isinstance(o, Number):
      return self.n <= o.n
    return self.n <= o
  def __gt__(self, o):
    if isinstance(o, Number):
      return self.n > o.n
    return self.n > o
  def __ge__(self, o):
    if isinstance(o, Number):
      return self.n >= o.n
    return self.n >= o
  def __int__(self):
    return int(self.n)
  def __float__(self):
    return float(self.n)
  def __str__(self):
    return str(self.n)
  __repr = __str__
  def __add__(self, o):
    if isinstance(o, Number):
      return Number(self.n + o.n)
    return Number(self.n + o)
  __radd__ = __add__
  def __sub__(self, o):
    if isinstance(o, Number):
      return Number(self.n - o.n)
    return Number(self.n - o)
  __rsub__ = __sub__
  def __mul__(self, o):
    if isinstance(o, Number):
      return Number(self.n * o.n)
    return Number(self.n * o)
  __rmul__ = __mul__
  def __truediv__(self, o):
    if o == 0:
      return 'ZeroDivisionError'
    if isinstance(o, Number):
      return Number(self.n / o.n)
    return Number(self.n / o)
  def __floordiv__(self, o):
    if o == 0:
      return 'ZeroDivisionError'
    if isinstance(o, Number):
      return Number(self.n // o.n)
    return Number(self.n // o)
    
obj2 = Number(5) #Fix test case bug

