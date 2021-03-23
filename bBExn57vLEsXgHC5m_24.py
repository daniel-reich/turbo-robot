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
​
  x1, y1 = lst[0][0], lst[0][-1]
  x2, y2 = lst[1][0], lst[1][-1]
  x3, y3 = lst[2][0], lst[2][-1]
​
  try:
    slope1 = (y2 - y1) / (x2 - x1)
  except ZeroDivisionError:
    slope1 = 'und'
  
  try:
    slope2 = (y3 - y2) / (x3 - x2)
  except ZeroDivisionError:
    slope2 = 'und'
​
  x = round((x1 + x2 + x3) / 3, 2)
  y = round((y1 + y2 + y3) / 3, 2)
​
  if slope1 == slope2:
    return True
  return False

