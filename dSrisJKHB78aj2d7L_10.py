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
  #c, b, a = math.ceil(perimeter / 3), math.ceil((perimeter - c) / 2), perimeter - (c + b)
  tri_list = []
  for c in range(math.ceil(perimeter / 3), math.floor(perimeter / 2) + 1):
    for b in range(math.ceil((perimeter - c) / 2), c + 1):
      a = perimeter - (c + b)
      p = perimeter / 2
      if (a + b + c == perimeter) and (float("%.5f" % (math.sqrt(p * (p - a) * (p - b) * (p - c)))) == area):
        tri_list.append([a, b, c])
  return tri_list

