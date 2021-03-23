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
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    x_left = max(x1, x2)
    x_right = min(x1 + w1, x2 + w2)
    y_bottom = max(y1, y2)
    y_top = min(y1 + h1, y2 + h2)
    return max(x_right - x_left, 0) * max(y_top - y_bottom, 0)

