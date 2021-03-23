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

def overlapping_rectangles(rect1, rect2):
    x, y, x1, y1 = rect1[0], rect1[1], rect1[0]+rect1[2],  rect1[1]+rect1[3]
    x_, y_, x1_, y1_ = rect2[0], rect2[1], rect2[0]+rect2[2],  rect2[1]+rect2[3]
    lx, ly = max(x,x_), max(y, y_)
    ux, uy = min(x1, x1_), min(y1, y1_)
    if (lx<=x1) & (ly<=y1):
        h, w = abs(ux-lx), abs(uy-ly)
        return h*w
    return 0

