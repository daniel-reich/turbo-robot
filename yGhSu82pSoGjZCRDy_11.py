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
  num = str(num)
  if len(num) > 1 and num != 'None':
    l = int(num[:len(num)//2])
    r = int(num[(len(num)//2):]) if not len(num)%2 else int(num[1 + (len(num)//2):])
    return 'left' if l > r else 'right' if r > l else 'balanced'
  return 'balanced'

