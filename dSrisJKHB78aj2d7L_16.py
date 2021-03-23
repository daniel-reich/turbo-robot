"""


Given the perimeter and the area of a triangle, devise a function that returns
the length of the sides of all triangles that fit those specifications. The
length of the sides must be integers. Sort results in ascending order.

    triangle(perimeter, area) ➞ [[s1, s2, s3]]

### Examples

    triangle(12, 6) ➞ [[3, 4, 5]]
    
    triangle(45, 97.42786) ➞ [[15, 15, 15]]
    
    triangle(70, 210) ➞ [[17, 25, 28], [20, 21, 29]]
    
    triangle(3, 0.43301) ➞ [[1, 1, 1]]

### Notes

N/A

"""

import math
def triangle(perimeter,area):
    triangles = []
    for a in range(1,math.floor(perimeter/3)+1):
        for b in range(a,math.floor((perimeter-a)/2)+1):
            c = perimeter - a - b
            s = perimeter/2
            if (s*(s-a)*(s-b)*(s-c) >= 0):
                if abs(math.sqrt(s*(s-a)*(s-b)*(s-c)) - area) < 0.0001:
                    triangles.append([a,b,c])
    return triangles

