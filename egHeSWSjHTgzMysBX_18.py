"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def half_a_fraction(fract):
  lst = [int(x) for x in fract.split("/")]
  if (lst[0]/2).is_integer():
    lst[0] = int(lst[0]/2)
  else:
    lst[1] = lst[1]*2
    
  return str(lst[0]) + "/" + str(lst[1])

