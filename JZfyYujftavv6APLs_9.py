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
    def __init__(self, numerator, denominator=1):
​
        if numerator == int(numerator) and denominator == int(denominator) and denominator != 0:
​
            self.a = numerator
            self .b = denominator
            min1 = min(abs(self.a), abs(self.b))
            c = 1
            for i in range(1, min1+1):
                if self.a % i == 0 and self.b % i == 0:
                    c = i
            self.a = self.a // c
            self.b = self.b // c
​
            self.f = 1
​
        else:
            self.f = 0
​
            print("Initialisation Failed")
​
    def __str__(self):
        if self.f == 1:
            if self.a * self.b < 0:
                return "- {}/{}".format(abs(self.a), abs(self.b))
            else:
                return "{}/{}".format(abs(self.a),abs(self.b))
        else:
            return "Initialisation Failed"
​
    def __mul__(self, other):
        n = self.a * other.a
        d = self.b * other.b
        return Fraction(n, d)
​
​
    def __sub__(self, other):
        n = self.a * other.b - other.a * self.b
        d = self.b * other.b
        return Fraction(n, d)
​
    def __le__(self, other):
        return self.a * other.b <= other.a * self.b
​
​
    def __ge__(self, other):
        return self.a * other.b >= other.a * self.b
​
    def __eq__(self, other):
        return self.decimal() == other.decimal()
​
    def __ne__(self, other):
       return self.a * other.b != other.a * self.b
​
​
    def __add__(self, other):
        n = self.a * other.b + other.a * self.b
        d = self.b * other.b
        return Fraction(n, d)
​
​
    def __truediv__(self, other):
        n = self.a * other.b
        d = self.b * other.a
        if d != 0:
            return Fraction(n, d)
​
​
    def __lt__(self, other):
        return self.a * other.b < other.a * self.b
​
    def __gt__(self, other):
        return self.a * other.b > other.a * self.b
​
​
​
    def decimal(self):
        x = self.a / self.b
        return round(x, 7)
​
​
​
    def fraction(decimal):
        if int(decimal) == decimal:
            return Fraction(int(decimal), 1)
        decimal = str(decimal)
        decimal_split = decimal.split('.')
        numerator = int(''.join(decimal_split))
        denominator = 10 ** len(decimal_split[1])
        return Fraction(numerator, denominator)

