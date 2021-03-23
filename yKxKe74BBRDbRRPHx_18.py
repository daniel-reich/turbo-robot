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
    self.num = num
    
  def __add__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a+b)
    
  def __sub__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a-b)
    
  def __rsub__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a-b)
    
  def __mul__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a*b)
    
  def __rmul__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a*b)
  
  def __truediv__(self,other):
    if other==0 or type(other)!=int and other.num==0:
      return 'ZeroDivisionError'
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a/b)
    
  def __floordiv__(self,other):
    if other==0 or type(other)!=int and other.num==0:
      return 'ZeroDivisionError'
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a//b)
    
  def __eq__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return a==b
  
  def __gt__(self,other):
    return self.num>other.num
  
  def __le__(self,other):
    return self.num<=other.num
    
  def __repr__(self):
    return "Number({})".format(self.num)
    
  def __str__(self):
    return str(self.num)
  
  def __int__(self):
    return int(self.num)
    
  def __float__(self):
    return float(self.num)

