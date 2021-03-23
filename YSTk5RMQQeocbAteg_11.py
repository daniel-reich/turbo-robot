"""


A tetrahedron is a pyramid with a triangular base and three sides. A
tetrahedral number is a number of items within a tetrahedron.

Create a function that takes an integer `n` and returns the `n`th tetrahedral
number.

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/Pyramid_of_35_spheres_animation.gif)

### Examples

    tetra(2) ➞ 4
    
    tetra(5) ➞ 35
    
    tetra(6) ➞ 56

### Notes

There is a formula for the `n`th tetrahedral number.

"""

def tetra(n):
  value = int((n*(n+1)*(n+2))/6)
  return value

