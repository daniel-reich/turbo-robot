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
  lst = [a,b,c]
  answer = max([ lst.count(x) for x in [a,b,c] ])
  return answer if answer != 1 else 0

