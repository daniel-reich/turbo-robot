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
    lis = txt.split("/")
    num1 = int(lis[0])
    num2 = int(lis[1])
    if not num1 % num2:
        return "{}".format(num1//num2)
    factors_of_num1 = [x for x in range(1, num1+1) if not num1 % x]
    factors_of_num2 = [y for y in range(1, num2+1) if not num2 % y]
    highest_common_factor = max(
        [a for a in factors_of_num1 if a in factors_of_num2])
    return "{}/{}".format(num1//highest_common_factor, num2//highest_common_factor)

