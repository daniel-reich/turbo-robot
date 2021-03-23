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
  a, b, c = lst
  if (a[0]==b[0]==c[0]) or (a[1]==b[1]==c[1]): return True
  else:
    try: 
      if (b[1]-a[1])/(b[0]-a[0])==(c[1]-a[1])/(c[0]-a[0]): return True
    except: pass
  return False

