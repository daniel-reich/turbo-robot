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

from math import sqrt
​
def triangle(perimeter,area):
  tris = []
  for a in range(1, perimeter//2+1):
    for b in range((perimeter-a)//2, a+1):
      #a>b>c
      c = perimeter-a-b
      cosine = (c*c - a*a - b*b)/(2*a*b)
      sine = sqrt(1 - cosine*cosine)
      if area == round(a*b*sine/2,5):
        if [b,c,a] not in tris and [c,b,a] not in tris:
          if b>c:
            tris.append([c,b,a])
          else:
            tris.append([b,c,a])
  return tris

