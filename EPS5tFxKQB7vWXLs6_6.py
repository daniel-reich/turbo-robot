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
  return -1 if h < 1 or w < 1 or h == 0 or w == 0 else h*w

