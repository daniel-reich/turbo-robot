"""


Write a function that takes the coordinates of three points in the form of a
2d array and returns the perimeter of the triangle. The given points are the
vertices of a triangle on a two-dimensional plane.

### Examples

    perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
    
    perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42
    
    perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28

### Notes

  * The given points always create a triangle.
  * The numbers in the argument array can be positive or negative.
  * Output should have 2 decimal places
  * This challenge is easier than it looks.

"""

class Triangle:
  class Line:
​
    def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2
​
      self.p1x = p1.x
      self.p1y = p1.y
​
      self.p2x = p2.x
      self.p2y = p2.y
​
      if self.p2y - self.p1y != 0:
        try:
          self.m = (self.p2y - self.p1y) / (self.p2x - self.p1x)
          self.b = self.p1y - (self.m * self.p1x)
          self.equation = 'y = {m}*x + {b}'.format(m = self.m, b = self.b)
        except ZeroDivisionError:
          self.m = None
          self.b = None
          self.equation = 'x = {}'.format(self.p1x)
      else:
        self.m = None
        self.b = None
        self.equation = 'y = {}'.format(self.p1y)
      
      self.length = ((self.p2x - self.p1x) ** 2 + (self.p2y - self.p1y) ** 2) ** .5
  class Point:
​
    def __init__(self, x, y):
      self.x = x
      self.y = y
  
  def __init__(self, points):
​
    self.p1 = Triangle.Point(points[0][0], points[0][1])
    self.p2 = Triangle.Point(points[1][0], points[1][1])
    self.p3 = Triangle.Point(points[2][0], points[2][1])
​
    self.l1 = Triangle.Line(self.p1, self.p2)
    self.l2 = Triangle.Line(self.p2, self.p3)
    self.l3 = Triangle.Line(self.p3, self.p1)
​
    self.perimeter = round(self.l1.length + self.l2.length + self.l3.length, 2)
​
def perimeter(lst):
​
  triangle = Triangle(lst)
  return triangle.perimeter

