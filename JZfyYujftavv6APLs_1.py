"""


Mathematically, a fraction can be defined as the ratio a/b, where a and b are
integers and b is non zero.

In this challenge, we are going to implement a Fraction class and some methods
to support arithmetic and comparison operations on them. Write a Fraction
class that meets the following requirements:

  *  **Initialisation:** Create a Fraction object with a as numerator and _b_ as denominator, e.g. `Fraction(5, 6)` where _a_ = 5 and _b_ = 6. Validate that _a_ and _b_ are both integers and _b_ is non-zero. If not, print the error message shown below and do not create any variables. The numerator and denominator should also be stored in factorized form, e.g. 4/6 should be stored as 2/3.

  *  **Representation:** It should be possible to print a Fraction or obtain a string representation of it via the `str` built-in function. For a positive fraction, this should return the string "x/y" e.g. "5/4". If the fraction is negative, return "- x/y" e.g. "- 5/9" (note the space after the `-` sign). If the fraction has failed to initialize, detect this (it shouldn't have any instance variables) and return the string "Initialisation Failed".

  *  **Arithmetic Operations:** Implement suitable methods to support `+`, `-`, `*`, and `/` operations between two fractions with the usual arithmetic meaning. Return the appropriate factorised Fraction e.g `Fraction(2, 3) * Fraction(2, 5)` should return `Fraction(4, 15)`. A division operation could result in a zero denominator and this should be catered for by printing the error message described in the initialization section and returning `None`. If the result of an operation is a negative fraction, return the numerator as the negative integer.

  *  **Comparison Operations:** Implement suitable methods to compare two Fraction objects using operators `==`,`!=`, `<`, `>`, `<=` and `>=` with the usual meanings. For `==`, apply a tolerance factor of _10^-7_.

  *  **Instance Method:** Implement instance method decimal. This should return the decimal equivalent of the Fraction object to up to seven decimal places e.g. `Fraction(1/4).decimal()` -> 0.25.

  *  **Class Method:** Implement class method fraction(decimal) which returns a Fraction object equivalent to decimal to up to seven decimal places e.g. `Fraction.fraction(2.5)` -> `Fraction(5, 2)`. If the parameter decimal is an integer, set the denominator in Fraction to 1.

### Examples

    str(Fraction(2, -3)) ➞ ""- 2/3"
    
    str(Fraction(3, 0)) ➞ "Initialisation Failed"
    # Should print "numerator must be an integer and denominator a non zero integer".
    
    Fraction(1, 5) + Fraction(3, 10) ➞ Fraction(1, 2)
    
    Fraction(5, 2) * Fraction(6, -10) ➞ Fraction(-3, 2)
    
    Fraction(0, 3) / Fraction(0, 5) ➞ None
    # Should print "numerator must be an integer and denominator a non zero integer".
    
    Fraction(-4, 5) > Fraction(-3, 5) ➞ False
    
    Fraction(10, 9) < Fraction(2, 1) ➞ True
    
    Fraction.fraction(11) ➞ Fraction(11, 1)
    
    Fraction(5, 9).decimal() ➞ 0.5555556

### Notes

You will need to use a technique called operator overloading to successfully
complete this challenge. This requires the use of what are termed _magic_ or
_dunder_ methods in Python ( **Resources** have a useful link for these). If
you need to brush up on arithmetic with fractions, there's a link for that
too.

"""

class Fraction:
  def __init__(self,a=0,b=1):
    if type(a)==int and type(b)==int and b!=0:
      x,y=a,b
      while y:x,y=y,x%y
      self.a=abs(a)//x*(1,-1)[Fraction.sign(a*b)=='-']
      self.b=abs(b)//x
  def __str__(self):
    try:return('- %s/%s'if Fraction.sign(self.a*self.b)else'%s/%s')%(abs(self.a),abs(self.b))
    except:return'Initialisation Failed'
  def __add__(self,f):
    x,y=self.b,f.b
    while y:x,y=y,x%y
    l=self.b*f.b//x
    return Fraction(l//self.b*self.a+l//f.b*f.a,l)
  def __truediv__(self,f):
    if f.a:return self*Fraction(f.b,f.a)
  __sub__=lambda self,f:self.__add__(-f)
  __neg__=lambda self:Fraction(-self.a,self.b)
  __mul__=lambda self,f:Fraction(self.a*f.a,self.b*f.b)
  __eq__=lambda self,f:self.a*f.b-self.b*f.a<10**-7
  __lt__=lambda self,f:self.a*f.b<self.b*f.a
  __gt__=lambda self,f:self.a*f.b>self.b*f.a
  __le__=lambda self,f:self.a*f.b<=self.b*f.a
  __ge__=lambda self,f:self.a*f.b>=self.b*f.a
  decimal=lambda self:round(self.a/self.b,7)
  @staticmethod 
  def sign(v):return('','-')[v<0]
  @classmethod
  def fraction(cls,v):
    v=str(round(v,7))
    return Fraction(int(v.replace('.','')),10**(len(v)-1))

