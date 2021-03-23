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
def fp_eq(n1, n2):
  return abs(n1 - n2) < 0.00001
​
def triangle(perimeter,area):
  res = []
  s = perimeter / 2
  test = area ** 2 / s
  for a in range(1, (perimeter // 3) + 1):
    for b in range(max(a, math.ceil(perimeter / 2 - a)), ((perimeter - a) // 2) + 1):
      c = perimeter - a - b
      val = (s-a)*(s-b)*(s-c)
      if fp_eq(val, test):
        res.append([a, b, c])
  return res

