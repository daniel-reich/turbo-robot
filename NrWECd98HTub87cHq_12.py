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
    zero = lambda a, b:  max(a) < min(b) or max(b) < min(a)
    x11, y11, x12, y12 = r1[0], r1[1], r1[0]+r1[2], r1[1]+r1[3]
    x21, y21, x22, y22 = r2[0], r2[1], r2[0]+r2[2], r2[1]+r2[3]
    if zero((x11,x12), (x21, x22)) or zero((y11,y12), (y21, y22)):
        return 0
    x1, x2 = sorted((x11, x12, x21, x22))[1:3]
    y1, y2 = sorted((y11, y12, y21, y22))[1:3]
    return (x2 - x1) * (y2 - y1)

