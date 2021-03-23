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

import math
def shortestDistance(txt):
 l = [int(s) for s in txt.split(',')]
 distance = math.sqrt( ((l[0]-l[2])**2)+((l[1]-l[3])**2) )
 return round(distance, 2)

