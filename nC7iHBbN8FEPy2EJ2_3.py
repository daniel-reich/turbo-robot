"""


Your task is to create a Circle constructor that creates a circle with a
radius provided by an argument. The circles constructed must have two getters
`getArea()` (PI _r^2) and`getPerimeter()` (2_PI*r) which give both respective
areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor
which you can use as a base example.

### Examples

    circy = Circle(11)
    circy.getArea()
    
    # Should return 380.132711084365
    
    circy = Circle(4.44)
    circy.getPerimeter()
    
    # Should return 27.897342763877365

### Notes

Round results up to the nearest integer.

"""

import math
​
class Circle:
​
  def __init__(self, radius = 0, perimeter = 0):
    self.radius = radius
    self.perimeter = perimeter
    
  def getArea(self):
    return math.pi * math.pow(self.radius, 2)
  
  def getPerimeter(self):
    return 2 * math.pi * self.radius

