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
  d=txt.split("/")
  b,c=int(d[0]), int(d[1])
  for i in range(b, 0, -1):
    if b%i==0 and c%i==0 and c/i==1:
      return str(int(b/c))
    elif b%i==0 and c%i==0:
      return str(int(b/i)) + "/" + str(int(c/i))
  return txt

