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

class Rectangle:
    def __init__(self, rect):
        x, y, width, height = rect[:]
        
        self.left = x
        self.right = x + width
        self.bottom = y
        self.top = y + height
​
​
def overlapping_rectangles(rect1, rect2):
    """Area of Overlapping Rectangles"""
    r1 = Rectangle(rect1)
    r2 = Rectangle(rect2)
    
    # Coordinates of the intersected rectangle
    left = max(r1.left, r2.left)
    right = min(r1.right, r2.right)
    bottom = max(r1.bottom, r2.bottom)
    top = min(r1.top, r2.top)
    
    # If they are not overlapping
    if left > right or bottom > top:
        return 0
        
    # Return the area (which is base * height)
    return ((right - left) * (top - bottom))

