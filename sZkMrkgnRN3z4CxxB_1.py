"""


Make a Rectangle class with four parameters, an **x** , a **y** (representing
the **top-left** corner of the rectangle), a **width** and a **height**
exclusively in that order.

Lastly, make a function `intersecting` that takes two Rectangle objects and
returns `True` if those objects are intersecting (colliding), else return
`False`.

### Examples

    a = Rectangle(10, 20, 100, 20)
    b = Rectangle(10, 40, 15, 20)
    c = Rectangle(50, 50, 20, 30)
    
    intersecting(a, b) ➞ True
    
    intersecting(a, c) ➞ False
    
    intersecting(b, c) ➞ True

### Notes

  * No negative values will be passed.
  * If it's a bit confusing, try imagining the rectangle with the given width and height and then place their top-left corner to the given x, y coordinates.

"""

class Rectangle:
  
  def __init__(self, x, y, width, height):
    self.x, self.y = x, y
    self.width, self.height = width, height
​
def intersecting(a, b):
  x = (a.x <= b.x and a.x + a.width >= b.x) or \
    (b.x <= a.x and b.x + b.width >= a.x)
  y = (a.y <= b.y and a.y + a.height >= b.y) or \
    (b.y <= a.y and b.y + b.height >= a.y)
  return x and y

