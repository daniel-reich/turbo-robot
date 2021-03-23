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
    a, b = txt.split("/")
    a = int(a)
    b = int(b)
    
    t = ggT(a,b)
    a = a//t
    b = b//t
    
    if b!=1:
        return str(a)+ "/" +str(b)
    else:
        return str(a)
    
    
def ggT(a, b):
    if b == 0:
        return a
    return ggT(b, a%b)

