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

def dist(line,x,y):
    from math import sqrt
    a=-eval(line[line.index("=")+1:line.index("x")])
    b=1
    c=-eval(line[line.index("x")+1:])
    return round((abs(a*x+b*y+c))/(sqrt(a*a+b*b)),2)

