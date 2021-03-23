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
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    
  def getedges(self):
    # create a dictionary of all edge coordinates
    top = { (a, self.y) : True for a in range(self.x, self.x+self.w) }
    bot = { (a, self.y+self.h) : True for a in range(self.x, self.x+self.w) }
    lf = { (self.x , a) : True for a in range(self.y, self.y + self.h) }
    rt = { (self.x+self.w , a) : True for a in range(self.y, self.y + self.h) }
    rect = {}
    rect.update(top)
    rect.update(bot)
    rect.update(lf)
    rect.update(rt)
    print(rect)
    return rect.keys()
    
def intersecting(a, b):
  b_coords = b.getedges()
  a_coords = a.getedges()
  for i in b_coords:
    if i in a_coords:
      return True
  return False

