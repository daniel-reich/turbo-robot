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
    splitTxt = txt.split("/")
    numer = int(splitTxt[0])
    denom = int(splitTxt[1])
    if numer % denom == 0:
        return str(round(numer/denom))
    else:
        gcd = round(max([numer, denom])/2)
        while gcd > 1:
            if numer % gcd == 0 and denom % gcd == 0:
                return str(round(numer/gcd)) + "/" + str(round(denom/gcd))
            gcd-=1
        return txt

