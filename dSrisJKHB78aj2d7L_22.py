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

def triangle(p,a):
  res = []
  for i in range(1,p//2+1):
    for j in range(i,p//2+1):
      try:
        if a == round((p/2*(p/2-i)*(p/2-j)*(p/2-(p-i-j)))**0.5,5):
          if sorted([i,j,p-i-j]) not in res:
            res.append(sorted([i,j,p-i-j]))
      except:
        continue
  return res

