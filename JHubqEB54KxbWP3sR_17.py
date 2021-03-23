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

from math import sqrt
​
def dist(line, x, y):
    imp = line.split('=')[1]
    a = eval(imp[0:imp.index('x')])
    c = eval(imp[imp.index('x') + 1:])
    return round((abs(a*x + c - y))/(sqrt(a*a+1)), 2)

