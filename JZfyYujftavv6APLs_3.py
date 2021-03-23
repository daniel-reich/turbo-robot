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

from fractions import gcd
import re
​
​
class Fraction:
​
    def __init__(self, num, den):
        if float(num).is_integer() and float(den).is_integer() and den != 0:
            self.sign = 1 if num * den > 0 else -1
            num = round(abs(num))
            den = round(abs(den))
            gcd_num_den = gcd(num, den)
            self.num = num // gcd_num_den
            self.den = den // gcd_num_den
            self.create = True
        else:
            self.create = False
​
    def __str__(self):
        return (('{}/{}'.format(self.num, self.den) if self.sign > 0
                else '- {}/{}'.format(self.num, self.den))
                if self.create else 'Initialisation Failed')
​
    def __eq__(self, other):
        return (round(self.sign * self.num / self.den, 7) ==
                round(other.sign * other.num / other.den, 7))
​
    def __gt__(self, other):
        return (round(self.sign * self.num / self.den, 7) >
                round(other.sign * other.num / other.den, 7))
​
    def __lt__(self, other):
        return (round(self.sign * self.num / self.den, 7) <
                round(other.sign * other.num / other.den, 7))
​
    def __ge__(self, other):
        return (round(self.sign * self.num / self.den, 7) >=
                round(other.sign * other.num / other.den, 7))
​
    def __le__(self, other):
        return (round(self.sign * self.num / self.den, 7) <=
                round(other.sign * other.num / other.den, 7))
​
    def __ne__(self, other):
        return (round(self.sign * self.num / self.den, 7) !=
                round(other.sign * other.num / other.den, 7))
​
    def __add__(self, other):
        return Fraction(self.sign * self.num * other.den +
                        other.sign * other.num * self.den, self.den * other.den)
​
    def __sub__(self, other):
        return Fraction(self.sign * self.num * other.den -
                        other.sign * other.num * self.den, self.den * other.den)
​
    def __mul__(self, other):
        return Fraction(self.sign * self.num * other.sign * other.num,
                        self.den * other.den)
​
    def __truediv__(self, other):
        if other.num != 0:
            return Fraction(self.sign * self.num * other.sign * other.den,
                            self.den * other.num)
​
    def decimal(self):
        return round(self.num / self.den, 7)
​
    @classmethod
    def fraction(cls, val):
        str_num = str(val)
        parts = dict()
        for pattern in [r'(?P<w>\d+)(?=\.)',
                        r'(?<=\.)(?P<b>\d+)(?=\(|$)',
                        r'(?<=\()(?P<p>\d+)(?=\))']:
            for m in re.finditer(pattern, str_num):
                parts.update(m.groupdict())
​
        if 'w' in parts and 'b' in parts and 'p' in parts:
            denominator = (10 ** len(parts['b'] + parts['p'])
                           - 10 ** len(parts['b']))
            numerator = (int(parts['w'] + parts['b'] + parts['p'])
                         - int(parts['w'] + parts['b']))
        elif 'w' in parts and 'b' in parts:
            denominator = 10 ** len(parts['b'])
            numerator = int(parts['w'] + parts['b'])
        elif 'w' in parts and 'p' in parts:
            denominator = 10 ** len(parts['p']) - 1
            numerator = int(parts['w'] + parts['p']) - int(parts['w'])
        gcd_num_den = gcd(numerator, denominator)
        denominator //= gcd_num_den
        numerator //= gcd_num_den
        return Fraction(numerator, denominator)

