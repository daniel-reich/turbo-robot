"""


Create a function that takes four tuples. The first three are (x, y)
coordinates of three corners of a triangle. Return `True` if the fourth tuple
— the (x, y) coordinates of a test point — lies within the triangle, `False`
if it doesn't.

### Examples

    within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) ➞ True
    
    within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) ➞ False
    
    within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) ➞ True

### Notes

N/A

"""

def within_triangle(p1, p2, p3, test):
​
  class Triangle:
​
    def __init__(self, p1, p2, p3):
      self.p1 = p1
      self.p2 = p2
      self.p3 = p3
​
      #Line 1
​
      x1 = self.p1[0]
      y1 = self.p1[1]
​
      x2 = self.p2[0]
      y2 = self.p2[1]
​
      try:
        m = (y2 - y1) / (x2 - x1)
​
        
        #y1 = mx + b
        b = y1 - (m * x1)
​
        self.l12 = 'y == {} * x + {}'.format(m, b)
      except ZeroDivisionError:
        self.l12 = 'x == {}'.format(x1)
​
      x3 = self.p3[0]
      y3 = self.p3[1]
​
      m = (y3 - y2) / (x3 - x2)
​
      b = y3 - (m * x3)
​
      self.l23 = 'y == {} * x + {}'.format(m, b)
​
      m = (y1 - y3) / (x1 - x3)
​
      b = y1 - (m * x1)
​
      self.l31 = 'y == {} * x + {}'.format(m, b)
​
    def is_on_boundary(self, test):
​
      x = test[0]
      y = test[1]
​
      t1 = eval(self.l12)
      t2 = eval(self.l23)
      t3 = eval(self.l31)
​
      tests = [t1, t2, t3]
​
      if True in tests:
        return True
      return False
    
    def is_within_triangle(self, test):
​
      x = test[0]
      y = test[1]
​
      x1 = self.p1[0]
      y1 = self.p1[1]
​
      x2 = self.p2[0]
      y2 = self.p2[1]
​
      x3 = self.p3[0]
      y3 = self.p3[1]
​
      a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
      b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
      c = 1 - a - b
​
      if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        return True
      else:
        return False
​
​
  triangle = Triangle(p1, p2, p3)
​
  return triangle.is_within_triangle(test)

