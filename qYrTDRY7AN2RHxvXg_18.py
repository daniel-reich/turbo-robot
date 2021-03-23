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
    p1 = (c**4 - 16*(A**2))
    return "Does not exist" if p1<0 else sorted([round(((c**2 + p1**0.5)/2)**0.5,3),round(((c**2 - p1**0.5)/2)**0.5,3)])

