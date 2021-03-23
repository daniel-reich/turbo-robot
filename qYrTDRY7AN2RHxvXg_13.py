"""


Consider a right triangle. Its area and hypotenuse are known.

Create a function that returns the two missing sides. The first input is the
area and the second input is the hypotenuse. Return your answer as a list (the
shorter side first). If there is no such right triangle, return `"Does not
exist"`.

### Examples

    f(3, 6) ➞ [1.015, 5.914]
    
    f(30, 12) ➞ [5.675, 10.574]
    
    f(30, 10) ➞ "Does not exist"

### Notes

Round your answer to three decimal places.

"""

from math import sqrt
def quad(a, b, c):
  return (-b + sqrt(b**2 - 4 * a * c))/(2*a)
  
​
def f(A, c):
  #a * b  = 2*A - > a**2*b**2 = 4A**2
  #a^2 + b^2 = c^2 -> a^4 + a^2*b^2 = a^2*c^2 -> a^4 - c^2a^2 + 4A^2 = 0
  try:
    a = sqrt(quad(1, -c**2, 4 * A**2))
  except ValueError:
    return "Does not exist"
  b = (2 * A)/a
  return list(sorted([round(s, 3) for s in (a, b)]))

