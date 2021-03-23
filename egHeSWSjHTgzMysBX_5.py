"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def fgc(a,b):
  if(a == 0):
    return b
  elif(b == 0):
    return a
  else:
    k = min(a,b)
    p = max(a,b)
    if(p%k == 0):
      return k
    else:
      r = p%k
      return (fgc(k,r))
​
def half_a_fraction(fract):
  ss = list(fract.split('/'))
  k1 = int(ss[0])
  k2 = int(ss[1])
  k2 = k2*2
  r = fgc(k1,k2)
  k1 = int(k1/r)
  k2 = int(k2/r)
  s = ""
  s = str(k1) + "/" + str(k2)
  return s

