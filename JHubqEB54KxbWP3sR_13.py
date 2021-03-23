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

def point_line_segment_distance(x1, y1, x2, y2, x3, y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1
​
    norm = px*px + py*py
​
    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)
​
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
​
    x = x1 + u * px
    y = y1 + u * py
​
    dx = x - x3
    dy = y - y3
​
    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance
​
    dist = (dx*dx + dy*dy)**.5
​
    return dist
​
def dist(line, x, y):
    x1 = -10**3
    x2 = 10**3
    line = line.replace('y=', '')
    line = line.replace('x(', 'x*(')
    for d in range(10):
        line = line.replace(str(d) + '(', str(d) + '*(')
        line = line.replace(str(d) + ')x', str(d) + ')*x')
        line = line.replace(str(d) + 'x', str(d) + '*x')
    y1 = eval(line.replace('x', str(x1)))
    y2 = eval(line.replace('x', str(x2)))
    d = point_line_segment_distance(x1, y1, x2, y2, x, y)
    return round(d, 2)

