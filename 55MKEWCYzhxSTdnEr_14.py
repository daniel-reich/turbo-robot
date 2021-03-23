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

def gcd_order(a, b):
    if b % a == 0:
        return a
    else:
        return gcd_order(b % a, a)
​
​
def gcd(a, b):
    if a > b:
       return gcd_order(b, a)
    return gcd_order(a, b)

