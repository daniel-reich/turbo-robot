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
  coor1 = get_coor(rect1)
  coor2 = get_coor(rect2)
  x1,y1 = max(coor1[0][0],coor2[0][0]),max(coor1[0][1],coor2[0][1])
  x2 = min(coor1[1][0],coor2[1][0])
  y2 = min(coor1[2][1],coor2[2][1])
  if x1>x2 or y1>y2:
    return 0
  width = x2-x1
  height = y2-y1
  return width*height
  
def get_coor(lst):
  x,y,w,h = lst
  return [(x,y),(x+w,y),(x,y+h),(x+w,y+h)]

