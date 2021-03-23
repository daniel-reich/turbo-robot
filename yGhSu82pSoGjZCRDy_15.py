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
  even_left_num = str(num)[0:(len(str(num)))//2]
  even_right_num = str(num)[len(str(num))//2:]
  odd_left_num = str(num)[0:(len(str(num)))//2]
  odd_right_num = str(num)[len(str(num))//2+1:]
  if num == None:
    return "balanced"
  elif len(str(num))%2 == 0:
    if even_left_num > even_right_num:
      return "left"
    elif even_left_num < even_right_num:
      return "right"
    else:
      return "balanced"
  elif len(str(num))%2 != 0:
    if odd_left_num > odd_right_num:
      return "left"
    elif odd_left_num < odd_right_num:
      return "right"
    else:
      return "balanced"

