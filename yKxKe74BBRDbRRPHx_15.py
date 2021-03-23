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
  def __init__(self, n): self.n = n
  __eq__ = lambda self, other: self.n == other
  __add__ = lambda self, other: self.n + other
  __radd__ = __add__
  __sub__ = lambda self, other: self.n - other
  __mul__ = lambda self, other: self.n * other
  __rmul__ = __mul__
  __truediv__ = lambda self, other: "ZeroDivisionError" if other == 0 else self.n / other
  __rtruediv__ = lambda self, other: "ZeroDivisionError" if self == 0 else other / self.n
  __int__ = lambda self: int(self.n)
  __float__ = lambda self: float(self.n)
  __str__ = lambda self: str(self.n)

