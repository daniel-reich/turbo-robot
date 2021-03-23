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

def triangle(p, area):
    const, sol, r = round(2*area**2/p, 3), [], range(1, round(p/2+0.1))
    sol = [tuple(sorted((a, b, p-a-b))) for a in r for b in r
           if (p/2-a)*(p/2-b)*(a+b-p/2)==const]
    return sorted([list(i) for i in set(sol)])

