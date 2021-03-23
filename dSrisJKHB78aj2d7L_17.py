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

import numpy as np
​
def area(a,b,c):
    s = (a+b+c)/2
    return np.sqrt(s*(s-a)*(s-b)*(s-c))
​
def triangle(p, a):
    lst = []
    for i in range(1,p//3+1):
        for j in range(i, (p-i)//2+1):
            k = p-i-j
            if not(i+j>k and j+k>i and k+i>j):
                continue
            if np.around(area(i,j,k),decimals=5) == a:
                lst.append([i,j,k])
    return lst

