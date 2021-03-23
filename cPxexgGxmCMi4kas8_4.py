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
    def __init__(self, lst=None):
        self.SetComponents(lst if lst else [0.0, 0.0, 0.0, 0.0])
​
    def GetComponents(self):
        return self.__components
​
    def SetComponents(self, lst):
        self.__components = lst
​
    def __add__(self, other):
        return FourVector([self.__components[i] + other.__components[i] for i in range(4)])
​
    def __sub__(self, other):
        return FourVector([self.__components[i] - other.__components[i] for i in range(4)])
​
    def __eq__(self, other):
        return all(self.__components[i] == other.__components[i] for i in range(4))
​
    def __str__(self):
        return "({}, {}, {}, {})".format(*map(lambda c: round(c, 3), self.__components))

