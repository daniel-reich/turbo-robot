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
  (x1, y1), (x2, y2), (x3, y3) = lst
  try:
    if x1 == x2 == x3 or y1 == y2 == y3:
      return True
    return (x1 - x2)/(y1 - y2) == (x2 - x3)/(y2 - y3)
  except ZeroDivisionError:
    return False

