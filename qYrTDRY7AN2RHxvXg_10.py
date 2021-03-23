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
  aa = 1
  bb = -1*c**2
  cc = (2*A)**2
  
  dd = bb**2-4*aa*cc
  if dd < 0:
    return 'Does not exist'
​
  w1 = (-bb+(dd)**.5)/2
  w2 = (-bb-(dd)**.5)/2
​
  z1 = round(w1**.5,3)
  z2 = round(w2**.5,3)
  myans = [z1,z2]
  return sorted(myans)

