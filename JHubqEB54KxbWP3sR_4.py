"""


Given the formula for a straight line `y = ax + b` and the x, y coordinates of
a point, find the distance between that point and the line. Round the result
to two decimal points.

### Examples

    dist("y=(-3/4)x-5/4", 5, 2) ➞ 5.6
    
    dist("y=(5+1/3)x-2.3", 1, 4) ➞ 0.18
    
    dist("y=2.2x-(3+1/5)", 3, -2) ➞ 2.23

### Notes

Check the **Resources**.

"""

def dist(line, x, y):
  a = line[2:line.index("x")]
  b = line[line.index("x")+1:]
  a = eval(a)
  b = eval(b)
  div = (1 + (a**2))**0.5
  r = (a * x) + (-1 * y) + b
  return round(abs(r)/div, 2)

