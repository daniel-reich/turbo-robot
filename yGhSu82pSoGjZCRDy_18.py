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
  l,r,b = "left", "right", "balanced"
  if not num:
    return b
  leng = int(len(str(num))/2)
  numl,numr = [int(x) for x in str(num)[:leng]],[int(x) for x in str(num)[leng if not len(str(num)) % 2 else leng+1:]]
  return b if sum(numl) == sum(numr) else l if sum(numl) > sum(numr) else r

