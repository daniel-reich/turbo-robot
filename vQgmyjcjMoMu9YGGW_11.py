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
  a, b = map(int, txt.split('/'))
  if a % b == 0:
    return str(a//b)
  for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
      return '{}/{}'.format(a//i, b//i)
  return txt

