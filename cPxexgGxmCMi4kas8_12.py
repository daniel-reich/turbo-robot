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

class FourVector(object):
    """docstring for FourVector."""
​
    def __init__(self, Components = [0.0, 0.0, 0.0, 0.0]):
        super(FourVector, self).__init__()
        self.Components = Components
​
    def GetComponents(self):
        return self.Components
​
    def SetComponents(self, NewComponents):
        self.Components = NewComponents
​
    def __add__(self, addend):
        return FourVector([x + y for (x, y) in zip(self.Components, addend.Components)])
​
    def __sub__(self, subtrahend):
        return FourVector([x - y for (x, y) in zip(self.Components, subtrahend.Components)])
​
    def __eq__(self, ElementToCompare):
        if self.Components == ElementToCompare.Components:
            return self
            
    def __str__(self):
        return "({}, {}, {}, {})".format(round(self.Components[0],3), round(self.Components[1],3), round(self.Components[2],3), round(self.Components[3],3))

