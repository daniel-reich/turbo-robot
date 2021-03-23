"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

def is_parallelogram(lst):
  xs = sorted([x[0] for x in lst])
  ys = sorted([y[1] for y in lst])
  is_x = abs(xs[1]-xs[0]) == abs(xs[3]-xs[2])
  is_y = abs(ys[1]-ys[0]) == abs(ys[3]-ys[2])
  return all([is_x, is_y])

