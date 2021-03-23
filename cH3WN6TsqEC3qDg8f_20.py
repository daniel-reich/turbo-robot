"""


Create a function that takes three numbers — the width and height of a
rectangle, and the radius of a circle and returns `True` if the rectangle can
fit inside the circle, `False` if it can't.

### Examples

    rectangle_in_circle(8, 6, 5) ➞ True
    
    rectangle_in_circle(5, 9, 5) ➞ False
    
    rectangle_in_circle(4, 7, 4) ➞ False

### Notes

N/A

"""

def rectangle_in_circle(w, h, radius):
  dist_to_corner = ((w/2)**2 + (h/2)**2)**0.5
  return dist_to_corner <= radius

