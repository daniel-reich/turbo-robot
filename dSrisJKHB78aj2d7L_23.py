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
​
def triangle(perimeter,area):
    ans = []
    for a in range(1, perimeter - 1):
        for b in range(1, perimeter - 1):
            c = perimeter - a - b
            sides = sorted([a, b, c])
            if a + b <= c or a + c <= b or b + c <= a:
                continue
            s = (a + b + c) / 2.
            A = math.sqrt(s * (s - a) * (s - b) * (s - c))
            if abs(A - area) < 1e-5 and sides not in ans:
                ans.append(sides)
    return ans

