"""


Create a function that returns the area of the overlap between two rectangles.
The function will receive two rectangles, each with the coordinates of the
lower left corner followed by the width and the height `rect = [x, y, width,
height]`.

### Examples

    overlapping_rectangles([ 2, 1, 3, 4 ], [ 3, 2, 2, 5 ]) ➞ 6
    
    overlapping_rectangles([ 2, -9, 11, 5 ], [ 5, -11, 2, 9 ]) ➞ 10
    
    overlapping_rectangles([ -8, -7, 4, 7 ],  [-5, -9, 4, 7 ]) ➞ 5

![Example 1](https://edabit-challenges.s3.amazonaws.com/ex1.png)

![Example 2](https://edabit-challenges.s3.amazonaws.com/ex2.png)

![Example 3](https://edabit-challenges.s3.amazonaws.com/ex3.png)

### Notes

  * Coordinates can be positive or negative integers.
  * Not all examples have overlaps.

"""

def overlapping_rectangles(r1, r2):
    l1,l2 = sorted([r1,r2],key=lambda x: x[0])
    m1,m2 = sorted([r1,r2],key=lambda x: x[1])  
    x = min(l1[2]-(l2[0]-l1[0]),l2[2]) if l2[0]-l1[0]<l1[2] else 0
    y = min(m1[3]-(m2[1]-m1[1]),m2[3]) if m2[1]-m1[1]<m1[3] else 0
    return x*y

