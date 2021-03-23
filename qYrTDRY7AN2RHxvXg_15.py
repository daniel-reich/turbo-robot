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

# https://edabit.com/challenge/qYrTDRY7AN2RHxvXg
​
import math
​
def f(a, h):
    x = h**4 - 16*a**2
    if x < 0:
        return "Does not exist"
​
    y = max((h**2 + math.sqrt(x))/2, (h**2 - math.sqrt(x))/2)
    s2 = math.sqrt(y)
    s1 = 2*a/s2
    l = [round(s1,3), round(s2,3)]
    l.sort()
    return l

