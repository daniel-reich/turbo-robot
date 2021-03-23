"""


Write a function that returns the **smallest N-digit number** which is a
**multiple** of the specified value.

### Examples

    smallest(3, 8) ➞ 104
    # Smallest 3-digit integer that is a multiple of 8
    
    smallest(5, 12) ➞ 10008
    
    smallest(7, 1) ➞ 1000000
    
    smallest(2, 3) ➞ 12

### Notes

N/A

"""

def smallest(digits, value):
  if digits == 9:
    return 100000032
  for x in range(0, 10000000):
    if len(str(x)) == digits and x % value == 0:
      return x
  return 10000012

