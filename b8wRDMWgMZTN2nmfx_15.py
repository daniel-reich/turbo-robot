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
  txt = a,b
  x = sum(2 if c == i else 0 for i in txt)
  if x == 4:
    return x -1
  if x == 0:
    t = c,b
    return sum(2 if a == i else 0 for i in t)
  return x

