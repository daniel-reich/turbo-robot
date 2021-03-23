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
    D = pow(c,4) - 16 * A * A 
    if D >= 0: 
        root1 = (c * c + sqrt(D))/2
        root2 = (c * c- sqrt(D))/2
        a = round(sqrt(root1),3) 
        b = round(sqrt(root2),3) 
        if b >= a: 
            return [a,b]
        else:
            return [b,a]
    else:
        return  "Does not exist"

