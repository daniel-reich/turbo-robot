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
    r=[]
    s=p/2
    for x in range(1,p//2+1):
        for y in range(int(s-x+1),p//2+1):
                z=p-x-y
                if round((s*(s-x)*(s-y)*(s-z))**.5,5)==a:
                    new=sorted((x,y,z))
                    if new not in r:
                        r.append(new)
    return sorted(r)

