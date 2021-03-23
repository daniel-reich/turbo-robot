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

import math
​
def f(A, c):
    D = c**4 - 16 * A**2
    if D >= 0:
        side1 = round( math.sqrt( (c**2 - math.sqrt(D)) / 2), 3)
        side2 = round( math.sqrt( (c**2 + math.sqrt(D)) / 2), 3)
        return [side1, side2]
    else:
        return "Does not exist"

