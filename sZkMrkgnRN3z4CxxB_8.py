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
  def __init__(self,x,y,w,h):
    self.x,self.y,self.w,self.h = x,y,w,h
    self.ul = [x,y]
    self.ll = [x,y-h]
    self.ur = [x+w,y]
    self.lr = [x+w,y-h]
​
def intersecting(a, b):
  for i in [a.ul,a.ll,a.ur,a.lr]:
    x,y = i
    if x>=b.ul[0] and y<=b.ul[1]:
      if x>=b.ll[0] and y>=b.ll[1]:
        if x<=b.ur[0] and y<=b.ur[1]:
          if x<=b.lr[0] and y>=b.lr[1]:
            return True
  return False

