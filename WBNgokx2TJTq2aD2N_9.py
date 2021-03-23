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
  def small_dig_finder(digits):
    n = '1'
    for num in range(digits-1):
      n += '0'
    return n
  
  minim = small_dig_finder(digits)
  maxim = small_dig_finder(digits) + '0'
  
  minim = int(minim)
  maxim = int(maxim)
  
  for n in range(minim, maxim):
    if n%value == 0:
      return n

