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

def f(A, c):
  k=c**2+4*A
  l=c**2-4*A
  if l>0:
    return [round((k**0.5-l**0.5)/2,3), round((k**0.5+l**0.5)/2,3)]
  else:
    return "Does not exist"

