"""


Create a function that takes a string of four numbers. These numbers represent
two separate points on a graph known as the x-axis (horizontal axis) and
y-axis (vertical axis).

The order of coordinates in the string corresponds as follows:

    "x1,y1,x2,y2"

Calculate the distance between x and y.

### Examples

    shortestDistance("1,1,2,1") ➞ 1
    
    shortestDistance("1,1,3,1") ➞ 2
    
    shortestDistance("-5,1,3,1") ➞ 8
    
    shortestDistance("-5,2,3,1") ➞ 8.06

### Notes

All floats fixed to two decimal places (e.g. 2.34).

"""

def shortestDistance(txt):
    p = txt.split(',')
    p1 = int(p[0]), int(p[1])
    p2 = int(p[2]), int(p[3])
    a, b = abs(p1[0]-p2[0])**2, abs(p1[1]-p2[1])**2
    c = (a+b)**0.5
    ans = round(c, 2)
    return ans

