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

def triangle(perimeter,area):
  solutions = []
  for s1 in range(1,perimeter):
    for s2 in range(1,perimeter-s1+1):
      s3 = perimeter - s1 - s2
      if s1+s2+s3 == perimeter:
        if round(16*(area**2)) == (2*(s1**2)*(s2**2))+(2*(s1**2)*(s3**2))+(2*(s2**2)*(s3**2))-s1**4-s2**4-s3**4:
          if sorted([s1,s2,s3]) not in solutions:
            solutions.append(sorted([s1,s2,s3]))
  return solutions

