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
    m = line[2:line.find('x')]
    line = line.replace('x', '*'+str(x))
    line = line.replace('y', '0')
    line += '-y'
    line = line.replace('y', str(y))
    return round(abs(eval(line[2:]))/((eval(m+'**2')+1)**0.5),2)

