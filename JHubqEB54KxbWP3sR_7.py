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

def dist(s, a, b):
  n = s.split('=')[1].find('x')
  i,j = s.split('=')[1][:n],1
  s1 = s.split('=')[1].replace('x','*'+str(a))+'-'+str(b)
  res =(eval(s1)/((eval(i)**2)+1)**0.5)
  return abs(round(res,2))

