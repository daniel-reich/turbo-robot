"""


Create a function that takes two numbers as arguments and returns the Greatest
Common Divisor (GCD) of the two numbers.

### Examples

    gcd(3, 5) ➞ 1
    
    gcd(14, 28) ➞ 14
    
    gcd(4, 18) ➞ 2

### Notes

The GCD is the highest number that can divide both arguments without a
remainder.

"""

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

