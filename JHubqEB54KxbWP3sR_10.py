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

def dist(line,x0,y0):
    '''
    Returns the shortest distance from line to the point at x0, y0
    '''
    # Uses Equation abs(c+ax0-y0))/sqrt(1 + a*a)
    c = eval(line[line.index('x')+1:])
    a = eval(line[line.index('=')+1:line.index('x')])
​
    return round(abs(c+a*x0-y0)/(1 + a*a)**0.5, 2)

