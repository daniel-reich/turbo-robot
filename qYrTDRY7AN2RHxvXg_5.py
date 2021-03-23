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
    if c**4 - 16*A**2 < 0:
        return 'Does not exist'
    else:
        height = sqrt((c**2 + sqrt(c**4 - 16*A**2))/2)
        base = sqrt(c**2 - height**2)
        rheight = round(height, 3)
        rbase = (round(base, 3))
        if rheight < rbase:
            return [rheight, rbase]
        else:
            return [rbase, rheight]

