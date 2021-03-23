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

class Number():
  def __init__(self,n):
    self.n = n
  def __eq__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n==a
  def __lt__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n<a
  def __le__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n<=a
  def __gt__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n>a
  def __ge__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n>=a
​
  def __int__(self):
    return int(self.n)
  def __float__(self):
    return float(self.n)
  def __str__(self):
    return str(self.n)
  def __repr__(self):
    return 'Number({})'.format(self.n)
  def __add__(self,a):
    return self.n+a.n if isinstance(a , Number) else self.n+a
  def __sub__(self,a):
    return self.n-a.n if isinstance(a , Number) else self.n-a
  def __rsub__(self,a):
    return a.n-self.n if isinstance(a , Number) else a-self.n
  def __mul__(self,a):
    return self.n*a.n if isinstance(a , Number) else self.n*a
  def __rmul__(self,a):
    return self.n*a.n if isinstance(a , Number) else self.n*a
  def __truediv__(self,a):
    return (self.n/a.n if a.n else 'ZeroDivisionError') if isinstance(a , Number) else (self.n/a if a else 'ZeroDivisionError')
  def __rtruediv__(self,a):
    return (a.n/self.n if self.n else 'ZeroDivisionError') if isinstance(a , Number) else (a/self.n if self.n else 'ZeroDivisionError')
  def __floordiv__(self,a):
    return self.n//a.n if isinstance(a , Number) else self.n//a

