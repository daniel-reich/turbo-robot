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

def f(A, h):
  d = (h**4 - 16*A*A)**0.5 / 2
  n = h*h / 2
  return "Does not exist" if type(d) == complex else [round((n-d)**0.5, 3), round((n+d)**0.5, 3)]

