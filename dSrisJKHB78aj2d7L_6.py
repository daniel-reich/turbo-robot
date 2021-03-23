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
  B=[]
  for i in range(1,perimeter-1):
    for j in range(1,perimeter-1):
      if type(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/2)-(perimeter-i-j)))
**(1/2))!=complex and round(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/
2)-(perimeter-i-j)))**(1/2), 5)==area:
        if sorted([i,j,perimeter-i-j]) not in B and perimeter-i-j>0:
          B.append(sorted([i,j,perimeter-i-j]))
  return B

