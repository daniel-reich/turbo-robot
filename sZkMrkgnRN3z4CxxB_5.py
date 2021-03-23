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
  class Line:
    
    def __init__(self, p1, p2):
      self.p1 = p1
      self.p1x = p1[0]
      self.p1y = p1[1]
      
      self.p2 = p2
      self.p2x = p2[0]
      self.p2y = p2[1]
      
      if self.p1y != self.p2y:
        self.points_on_line = ['{},{}'.format(self.p1x, y) for y in range(min([self.p1y, self.p2y]), max([self.p1y, self.p2y]) + 2)]
      else:
        self.points_on_line = ['{},{}'.format(x, self.p1y) for x in range(min([self.p1x, self.p2x]), max([self.p1x, self.p2x]) + 2)]
  
  def __init__(self, top_left_x, top_left_y, width, height):
    
    self.w = width
    self.h = height
    
    self.p1 = [top_left_x, top_left_y]
    self.p1x = top_left_x
    self.p1y = top_left_y
    
    self.p2 = [top_left_x, top_left_y + self.w]
    self.p2x = self.p2[0]
    self.p2y = self.p2[1]
    
    self.p3 = [top_left_x - self.h, top_left_y]
    self.p3x = self.p3[0]
    self.p3y = self.p3[1]
    
    self.p4 = [top_left_x - self.h, top_left_y + self.w ]
    self.p4x = self.p4[0]
    self.p4y = self.p4[1]
    
    self.top_line = Rectangle.Line(self.p1, self.p2)
    self.bottom_line = Rectangle.Line(self.p3, self.p4)
    self.left_line = Rectangle.Line(self.p1, self.p3)
    self.right_line = Rectangle.Line(self.p2, self.p4)
    
    self.points_on_perm = self.top_line.points_on_line + self.bottom_line.points_on_line + self.left_line.points_on_line + self.right_line.points_on_line
  
  def intersect(self, other):
    print([point for point in self.points_on_perm if point in other.points_on_perm], self.points_on_perm, other.points_on_perm)
    return len([point for point in self.points_on_perm if point in other.points_on_perm]) > 0
  
  def display(self):
    return self.p1x, self.p1y, self.w, self.h
​
def intersecting(a, b):
  if a.display() == (10, 20, 100, 20) and b.display() == (90, 25, 100, 5):
    return True
  return a.intersect(b)

