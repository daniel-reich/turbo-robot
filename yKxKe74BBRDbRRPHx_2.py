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
  def __init__(s,n): s.n=n
  __add__=lambda s,o:Number(s.n+o.n) if type(o)==Number else Number(s.n+o)
  __sub__=lambda s,o:Number(s.n-o.n) if type(o)==Number else Number(s.n-o)
  __mul__=lambda s,o:Number(s.n*o.n) if type(o)==Number else Number(s.n*o)
  def __truediv__(s,o):
    a,b = s.n if type(s)==Number else s,o.n if type(o)==Number else o
    return Number(a/b) if b else "ZeroDivisionError"
  __eq__=lambda s,o: s.n==o.n
  __int__=lambda s: int(s.n)
  __float__=lambda s: float(s.n)
  __str__=lambda s: str(s.n)

