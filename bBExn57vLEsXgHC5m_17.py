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
  
  if (lst[0][0] == lst[1][0] == lst[2][0]):
    return True
    
  if (lst[0][1] == lst[1][1] == lst[2][1]):
    return True
  
  Difference_A1 = lst[0][0] - lst[1][0]
  Difference_A2 = lst[0][1] - lst[1][1]
  
  if (Difference_A2 == 0):
    return False
  
  Difference_B1 = lst[1][0] - lst[2][0]
  Difference_B2 = lst[1][1] - lst[2][1]
  
  if (Difference_B2 == 0):
    return False
  
  Slope_A = Difference_A1 / Difference_A2
  Slope_B = Difference_B1 / Difference_B2
  
  if (Slope_A == Slope_B):
    return True
  else:
    return False

