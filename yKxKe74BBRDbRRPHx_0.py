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
  def __init__(self,v):self.v=v
  __eq__=lambda self,n:self.v==n.v if type(n)==Number else self.v==n
  __add__=lambda self,n:Number(self.v+n.v)if type(n)==Number else Number(self.v+n)
  __sub__=lambda self,v:Number(self.v-v)
  __rsub__=lambda self,v:Number(v-self.v)
  __mul__=lambda self,n:Number(self.v*n.v)if type(n)==Number else Number(self.v*n)
  __rmul__=__mul__
  __truediv__=lambda self,n:Number(self.v/n.v)if n else'ZeroDivisionError'
  __floordiv__=lambda self,n:Number(self.v//n.v)if n else'ZeroDivisionError'
  __str__=lambda self:str(self.v)
  __repr__=lambda self:'Number(%s)'%self.v
  __int__=lambda self:int(self.v)
  __float__=lambda self:float(self.v)
  __gt__=lambda self,n:self.v>n.v
  __le__=lambda self,n:self.v<=n.v

