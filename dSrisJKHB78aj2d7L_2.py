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

def triangle(peri, area):
    def heron(a, b, c):
        s = (a + b + c) / 2
        aa = (s * (s - a) * (s - b) * (s - c))
        if aa > 0:
            return round(aa**.5, 5)
​
    valid_triangles = []
    for s1 in range(1, peri // 2 + 1):
        for s2 in range(1, peri - s1):
            s3 = peri - s1 - s2
            if heron(s1, s2, s3) == area:
                valid_triangle = sorted([s1, s2, s3])
                if valid_triangle not in valid_triangles:
                    valid_triangles.append(valid_triangle)
    return valid_triangles

