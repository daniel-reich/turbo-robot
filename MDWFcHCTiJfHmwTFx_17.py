"""


Create a function to find only the root value of `x` in any quadratic equation
`ax^2 + bx + c`. The function will take three arguments:

  * `a` as the coefficient of `x^2`
  * `b` as the coefficient of `x`
  * `c` as the constant term

### Examples

    quadratic_equation(1, 2, -3) ➞ 1
    
    quadratic_equation(2, -7, 3) ➞ 3
    
    quadratic_equation(1, -12, -28) ➞ 14

### Notes

  * Quadratic equation is always guaranteed to have a root.
  * Check the **Resources** tab for more information on quadratic equations.
  * Calculate only the root that sums the square root of the discriminant, not the one that subtracts it.
  * Round the value / return only integer value.

"""

import math
def quadratic_equation(a, b, c):
  p_ = (b/a)/2
  q = c/a
  return (-p_)+math.sqrt(p_*p_-q)

