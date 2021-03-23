"""


Create a function that finds a root of a polynomial curve. Do this using the
Newton-Raphson method.

  * Your input will be a list of coefficients for a 3rd order polynomial: `c(0)*x^3 + c(1)*x^2 + c(2)*x + c(3)`
  * Round your answer to three decimal places (nearest 0.001). Choose x = 0.0 as an initial guess. Twenty iterations of the algorithm are sufficient for accuracy.
  * The Newton-Raphson method uses the generic derivative **df/dx**. This can be calculated analytically for a polynomial, or numerically using a small step of dx (such as 0.0001). See the **Resources** tab for more info.

### Examples

    newton_raphson([0.0, -0.1, -0.2, 0.3]) ➞ 1.000
    
    newton_raphson([-0.1, 0.4, 0.1, -0.8]) ➞ 3.681
    
    newton_raphson([0.2, -0.6, 1.5, -2.7]) ➞ 2.295

### Notes

N/A

"""

def newton_raphson(c):
  x=0.0
  for i in range(20):
    x=x-(c[0]*x**3+c[1]*x**2+c[2]*x+c[3])/(3*c[0]*x**2+2*c[1]*x+c[2])
  return round(x,3)

