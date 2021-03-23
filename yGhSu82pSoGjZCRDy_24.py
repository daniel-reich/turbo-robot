"""


A number is **left-heavy** if the digits on the left side are larger than the
digits on the right. It is **right-heavy** if the digits on the right side are
larger than the digits on the left. Else, it is **balanced**.

Create a function that takes in an integer and classifies it into one of the
three mutually exclusive categories: **left** , **right** or **balanced**. For
inputs with an odd number of integers, ignore the fulcrum (the middle number).

### Examples

    seesaw(3449) ➞ "right"
    # since 34 < 49
    
    seesaw(1143113) ➞ "left"
    # since 114 > 113 (3 is the fulcrum)
    
    seesaw(585585) ➞ "balanced"
    # since 585 == 585

### Notes

If input is `None` return `"balanced"`.

"""

def seesaw(num):
  string = str(num)
  if len(string) == 1 or len(string) == 0 or num == None:
    return 'balanced'
  else:
    length = len(string) // 2
    l_s = string[:length]
    r_s = string[0-length:]
    if int(l_s) > int(r_s):
      return 'left'
    elif int(l_s) < int(r_s):
      return 'right'
    elif int(l_s) == int(r_s):
      return 'balanced'

