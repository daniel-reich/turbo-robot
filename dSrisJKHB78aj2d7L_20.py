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

def triangle(p, A):
    '''
    Returns a list of lists [a,b,c] where a, b and c are sides of a triangle
    in increasing order such that a+b+c = p and the triangle's area = A
    '''
    TOL = 0.00001  # tolerance on area checks
    triangles = []
    s = p / 2
​
    for a in range(1, p//3 + 1):
        for b in range(1, (p-a)//2 + 1):
            c = p - a - b
            area = (s * (s - a) * (s - b) * (s - c)) **0.5
            if abs(A - area) <= TOL:
                t = sorted([a, b, c])
                if t not in triangles:
                    triangles.append(t)
​
    return triangles

