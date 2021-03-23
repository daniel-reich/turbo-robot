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
      l1, b1, r1, t1 = rect1[0], rect1[1], rect1[0] + rect1[2], rect1[1] + rect1[3];
      l2, b2, r2, t2 = rect2[0], rect2[1], rect2[0] + rect2[2], rect2[1] + rect2[3];
      if r2 < l1 or r1 < l2 or t2 < b1 or t1 < b2:
          return 0
      return abs((min(r2, r1) - max(l2, l1)) * (min(t2, t1) - max(b2, b1)))

