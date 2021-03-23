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
  a=[(rect1[0]+i,rect1[1]+j)for j in range(rect1[3]+1) for i in range(rect1[2]+1)]
  b=[(rect2[0]+i,rect2[1]+j)for j in range(rect2[3]+1) for i in range(rect2[2]+1)]
  if set(a)&set(b):
    c=set(a)&set(b)
    x=max([i[0]for i in c])-min([i[0]for i in c])
    y=max([i[1]for i in c])-min([i[1]for i in c])
    return (x*y)
  else:
    return 0

