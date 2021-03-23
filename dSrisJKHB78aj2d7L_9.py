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

def triangle(perim, area):
    s = perim / 2
    result = []
    for a in range(1, int(perim / 3 + 1)):
        for b in range(a, int((perim - a) / 2 + 1)):
            c = perim - a - b
            # Heron squared
            h = s * (s-a) * (s-b) * (s-c)
            if h > 0 and round(h**0.5, 5) == area:
                result.append([a,b,c])
    return result

