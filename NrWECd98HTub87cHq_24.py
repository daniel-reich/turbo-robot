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
  x1,y1,w1,l1=rect1
  x2,y2,w2,l2=rect2
  A=[]
  for i in range(x1, x1+w1):
    for j in range(y1, y1+l1):
      A.append((i,j))
  B=[]
  for i in range(x2, x2+w2):
    for j in range(y2, y2+l2):
      B.append((i,j))
  return len(set(A)&set(B))

