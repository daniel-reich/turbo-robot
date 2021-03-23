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
    ix = line.index('x')
    m, c = eval(line[2:ix]), eval(line[ix+1:])
    xi = (y * m + x - c * m) / (m * m + 1)
    yi = xi * m + c
    return round(((x - xi)**2 + (y - yi)**2)**0.5, 2)

