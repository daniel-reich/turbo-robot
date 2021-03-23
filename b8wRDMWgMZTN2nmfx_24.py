"""


Create a function that takes three integer arguments `(a, b, c)` and returns
the amount of integers which are of equal value.

### Examples

    equal(3, 4, 3) ➞ 2
    
    equal(1, 1, 1) ➞ 3
    
    equal(3, 4, 1) ➞ 0 

### Notes

Your function must return 0, 2 or 3.

"""

def equal(a, b, c): 
  if a == b:
    return 3 if a == c else 2
  elif a == c: 
    return 2 
  elif b == c:
    return 2 
  return 0

