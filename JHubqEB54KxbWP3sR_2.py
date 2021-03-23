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

import math
def dist(line, x, y):
    b = 1
    l = line.split("x")
    c = -eval(l[1])
​
​
    for i in l:
        if "y=" in i:
            a = -eval(i[2::])
​
    k = abs((a * x) + (b * y) + (c))
    g = (math.sqrt((a * a) + (b * b)))
    return round(k / g, 2)

