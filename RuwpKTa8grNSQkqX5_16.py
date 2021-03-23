"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def fractions(decimal):
    a, b = decimal.split('.')
    a = int(a)
    c, d = b.replace(')', '').split('(')
    n = len(d)
    m = len(c)
    d = int(d)
    if m == 0:
        # repeat starts immediately after decimal point:
        denom = 10**n - 1
        num = a * denom + d
        g = gcd(num, denom)
        denom //= g
        num //= g
        return str(num) + '/' + str(denom)
    else:
        # repeat does NOT start immediately after decimal point:
        c = int(c)
        f1 = 10**(n+m)
        f2 = 10**m
        f3 = 10**n
        denom = f1 - f2
        num = a * (f1 - f2) + c * f3 + int(d) - int(c)
        g = gcd(num, denom)
        denom //= g
        num //= g
        return str(num) + '/' + str(denom)

