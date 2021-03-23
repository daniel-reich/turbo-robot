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

def simplify(st):
    from fractions import gcd
    st = st.split('/')
    numer = int(st[0]);denom = int(st[1])
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (int(numer / common_divisor), int(denom / common_divisor))
    if reduced_den == 1:
        return str(reduced_num)
    elif common_divisor == 1:
        return str(numer)+'/'+str(denom)
    else:
        return "%d/%d" % (reduced_num, reduced_den)

