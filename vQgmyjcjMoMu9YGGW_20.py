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
  n = int(txt[:txt.index('/')])
  m = int(txt[txt.index('/')+1:])
  if n%m == 0:
    return str(n//m)
  for i in range(min(m,n), 0, -1):
    if m%i == 0 and n%i == 0:
      return '{}/{}'.format((n//i),(m//i))

