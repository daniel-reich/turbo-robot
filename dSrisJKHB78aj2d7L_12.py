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
    u=perimeter/2
    answer=[]
    for a in range(1, perimeter-1):
        for b in range(1, perimeter-1):
            c=perimeter-a-b
            if a+b>c and a+c>b and b+c>a and sorted ([a,b,c]) not in answer and round(u*(u-a)*(u-b)*(u-c), 0)==round(area**2, 0): 
                answer.append(sorted([a, b, c]))    
    return answer

