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
  limit = perimeter//2 + 1
  pos_val = []
  for i in range(1,limit):
    for j in range(1,i+1):
        k = perimeter-(i+j)
        m = max(i,j,k)
        if m<=(perimeter-m):  
          s=perimeter/2
          if area == round((s*(s-i)*(s-j)*(s-k))**0.5,5):
            temp = sorted([k,j,i])
            if pos_val.count(temp)==0:
              pos_val.append(temp)
  pos_val.sort(key=lambda x:x[0])
  return pos_val

