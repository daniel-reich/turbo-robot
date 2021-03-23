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
def f(A, c):
  
  try:
    y = sqrt((c**2 - sqrt(c**4 - 16*A**2))/2)
  except:
    return "Does not exist"
  x = 2*A/y
  
  
  l = sorted([x,y])
  
  return [round(l[0],3),round(l[1],3)]

