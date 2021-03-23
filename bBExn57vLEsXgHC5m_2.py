"""


Create a function that returns `True` if three points belong to the same line,
and `False` otherwise. Each point is represented by a list consisting of an x-
and y-coordinate.

### Examples

    same_line([[0, 0], [1, 1], [3, 3]]) ➞ True
    
    same_line([[-2, -1], [2, 1], [0, 0]]) ➞ True
    
    same_line([[-2, 0], [-10, 0], [-8, 0]]) ➞ True
    
    same_line([[0, 0], [1, 1], [1, 2]]) ➞ False
    
    same_line([[3, 4], [3, 5], [6, 6]]) ➞ False

### Notes

Note the special case of a vertical line.

"""

def same_line(lst):
  x1,y1=lst[0]
  x2,y2=lst[1]
  x3,y3=lst[2]
  if x1==x2 and x2==x3: return True
  if x2-x1==0 or x3-x2==0: return False
  return ((y2-y1)/(x2-x1))==((y3-y2)/(x3-x2))

