"""


Create a function that calculates the area of a rectangle. If the arguments
are invalid, your function must return `-1`.

### Examples

    area(3, 4) ➞ 12
    
    area(10, 11) ➞ 110
    
    area(-1, 5) ➞ -1
    
    area(0, 2) ➞ -1

### Notes

N/A

"""

def area(h, w):
  if min(h,w)<=0:
    return -1
  return h*w
