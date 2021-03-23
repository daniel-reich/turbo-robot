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
  lst = [a, b, c]
  if lst.count(a) >= 2:
    return lst.count(a)
  elif lst.count(b) >=2:
    return lst.count(b)
  elif lst.count(c) >= 2:
    return lst.count(c)
  else:
    return 0

