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

def herons_2(a, b, c):
    s = (a + b + c) / 2
    return s * (s-a) * (s-b) * (s-c)
​
def triangle(perimeter, area):
    area_2 = area ** 2
    margin = 0.001
    all_sides = set()
    for i in range(perimeter - 2, 0, -1):
        for j in range(perimeter - i - 1, 0, -1):
            k = perimeter - i - j
            if abs(herons_2(i, j, k) - area_2) < margin:
                all_sides.add(tuple(sorted((i, j, k))))
    return [list(s) for s in sorted(all_sides)]

