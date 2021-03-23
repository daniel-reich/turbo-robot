"""


This is the first challenge of the "Four Vectors" collection. Four Vectors are
vectors with four components that are used to describe relativistic physics.
For details please refer to [this wiki
entry](https://en.wikipedia.org/wiki/Four-vector).

In this challenge, create a class `FourVector` with the following properties:

  * If called with a list of length 4 as a parameter, it uses the list entries as components of the FourVector (FV) instance.
  * If called without a parameter, the components should be `[0.0, 0.0, 0.0, 0.0]`.
  * Getter and Setter methods `GetComponents` and `SetComponents`, see test cases
  * Methods two add and subtract two FV instances.
  * Support comparing two Four Vectors.
  * Support printing a FV in the form `(0.5, 1.0, -2.0, 10.0)` where the components are rounded to three decimal places.

Consider using magic methods like `__add__`, `__eq__` and `__str__` to solve
the last three bullet points.

### Examples

    v = FourVector([1, 2, 3, 4])
    print(v) ➞ (1, 2, 3, 4)
    
    v2 = FourVector([1, 0, 1, 0])
    print(v + v2) ➞ (2, 2, 4, 4)

### Notes

Please save your `FourVector` class for later use, we will add new methods in
upcoming challenges in this series!

"""

class FourVector:
​
  def __init__(self, points = [0,0,0,0]):
    self.points = points
  
    self.A = points[0]
    self.B = points[1]
    self.C = points[2]
    self.D = points[3]
  
  def __add__(self, other):
​
    return FourVector([(self.A + other.A), (self.B + other.B), (self.C + other.C), (self.D + other.D)])
  
  def __sub__(self, other):
    return FourVector([(self.A - other.A), self.B - other.B, self.C - other.C, self.D - other.D])
​
  def GetComponents(self):
    return self.points
​
  def SetComponents(self, components):
    self.points = components
​
    self.A = components[0]
    self.B = components[1]
    self.C = components[2]
    self.D = components[3] 
​
    return True
  
  def __str__(self):
    return '({}, {}, {}, {})'.format(round(self.A,3), round(self.B,3), round(self.C,3), round(self.D, 3))
​
  def __eq__(self, other):
    return  v0a

