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
  repeat = True
  txt = txt.split("/")
  a, b = int(txt[0]), int(txt[1])
  if int(a / b) == a / b:
    return (str(int(a / b)))
  
  while repeat:
    repeat = False
    for i in range(2, a + 1):
      if (int(a / i) == a / i) and (int(b / i) == b / i):
        a = int(a / i)
        b = int(b / i)
        repeat = True
​
  return (str (a) + "/" + str(b))

