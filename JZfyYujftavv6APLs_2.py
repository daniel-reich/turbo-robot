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
​
    def __init__(self, numerator, denominator):
        '''
        Create a fraction object.
        '''
        try:
            assert isinstance(numerator,int) and isinstance(denominator,int)\
            and denominator != 0,'numerator must be an integer and denominator a non zero integer' 
            self.num, self.denom = self.factorise(numerator, denominator)
        except AssertionError as e:
            print(e)
            
    def __str__(self):
        '''
        Returns a string representation of this fraction
        '''
        try:
            sign = '- ' if self.num < 0 else ''
            return sign + str(abs(self.num)) + '/' + str(self.denom)
        except AttributeError:
            return 'Initialisation Failed'   # can happen if attempt to create Fraction with zero denominator
​
    def gcd(self, a, b):
        '''
        Return the gcd of integers a and b 
        '''
        a, b = abs(a), abs(b)
        
        while b != 0:
            a, b = b, a % b
​
        return a
​
    def lcm(self, other):
        '''
        Return the lcm of the denominators of self and other
        '''
        return abs(self.denom) * abs(other.denom) // self.gcd(self.denom, other.denom)
​
    def factorise(self, num, denom):
        '''
        Returns numerator and denominator in factorised form
        If fraction is negative, sets numerator -ve and denominator +ve
        '''
        a = abs(num)
        b = abs(denom)
        factor = self.gcd(a, b)
        adj = -1 if num < 0 and denom > 0 or num > 0 and denom < 0 else 1
        return a // factor * adj, b // factor
            
​
    def __add__(self, other):
        '''
        Adds this fraction to fraction other and returns the resulting fraction
        '''
        multiplier = self.lcm(other)
        new_num = multiplier // self.denom * self.num + \
                  multiplier // other.denom * other.num
        new_num, new_denom = self.factorise(new_num, multiplier)
        return Fraction(new_num, new_denom)
​
    def __sub__(self, other):
        '''
        Subtracts fraction other from this one.
        Returns the resulting fraction
        '''
        return self + Fraction(-other.num, other.denom) # =  + - other
​
    def __mul__(self, other):
        '''
        Multiplies this fraction by fraction other
        Returns the resulting fraction
        '''
        num, denom = self.factorise(self.num*other.num, self.denom*other.denom) 
        return Fraction(num, denom)
​
    def __truediv__(self, other):
        '''
        Divides fraction self by fraction other
        Returns the resulting fraction
        '''
        if other.num != 0:  # check for divide by zero
            return self * Fraction(other.denom, other.num) # a/b / c/d is a/b * d/c
               
        print('numerator must be an integer and denominator a non zero integer')
        return None
​
    def __eq__(self, other):
        '''
        Returns True if self and other have the same values
        within a tolerance of 10^-7
        '''
        tolerance = 10**-7
        return abs(self.num / self.denom - other.num / other.denom) <= tolerance
​
    def __ne__(self, other):
        '''
        Returns True if self and other do not have the same values
        within a tolerance of 10^-7
        '''
        tolerance = 10**-7
        return abs(self.num / self.denom - other.num / other.denom) > tolerance
​
    def __lt__(self, other):
        '''
        Returns True if self's value < other's
        '''
        return self.num / self.denom < other.num / other.denom
​
    
    def __gt__(self, other):
        '''
        Returns True if self's value > other's
        '''
        return self.num / self.denom > other.num / other.denom
​
    def __le__(self, other):
        '''
        Returns True if self's value <= other's
        '''
        return self == other or self < other
​
    def __ge__(self, other):
        '''
        Returns True if self's value >= other's
        '''
        return self == other or self > other
​
    def decimal(self):
        '''
        Returns the decimal equivalent of this fraction
        '''
        return round(self.num / self.denom, 7)
​
    @staticmethod
    def fraction(decimal):
        '''
        Returns a Fraction object equivalent to decimal.
        If decimal is an integer, returns 1 as the denominator,
        otherwise equivalent of decimal rounded to 7 decimal places.
        '''
        if isinstance(decimal, int):
            return Fraction(decimal, 1)
​
        mult = 10**7 
        decimal = round(decimal, 7)
        return Fraction(int(decimal * mult), mult)

