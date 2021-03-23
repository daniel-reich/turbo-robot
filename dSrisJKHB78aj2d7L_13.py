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
  print(perimeter,area)
  result=[]
  for i in range(perimeter//2):
    a =i+1
    b_c = perimeter - a
    for j in range(b_c):
      b= j + 1
      c= b_c - b 
      
      P=a+b+c
      p=(P)/2
      A= (p*(p-a)*(p-b)*(p-c))**0.5
      if not(isinstance(A, complex )) and round(A,5) == area :
        r=[a,b,c]
        r.sort()
        if r not in result:
          result.append(r)
  if len(result)>1:
    result.sort(key = lambda x: x[0])
  return (result)

