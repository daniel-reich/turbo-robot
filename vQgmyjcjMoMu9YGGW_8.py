"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

def simplify(txt):
    gcd = lambda a,b: a if b == 0 else gcd(b,a%b)
    num = [int(n) for n in txt.split('/')]
    d = gcd(*num)
    num = [n//d for n in num]
    if num[-1] == 1: num.pop()
    return '/'.join(str(n) for n in num)

