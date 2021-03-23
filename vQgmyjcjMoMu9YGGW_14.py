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
    a, b = int(txt[:txt.index('/')]), int(txt[txt.index('/') + 1:]) # a: numerator, b: denominator
    if a % b == 0: return str(int(a / b)) # Can be divided
​
    divisible = [i for i in range(2, min(a + 1, b)) if a % i == 0 and b % i == 0]
    # Makes list of numbers that both a and b can be divided with
    
    if divisible == []: return txt # No divisibles, return original txt
​
    a, b = int(a / divisible[-1]), int(b / divisible[-1])
    return '{}/{}'.format(a, b) # Divide both a and b, put them together, return

