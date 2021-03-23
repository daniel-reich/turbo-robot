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
​
    import math
​
    c_sqr = pow(c, 2)
    A_COF = (4) * pow(A, 2)
​
    try:
        t_1 = (c_sqr - math.sqrt((pow(c_sqr, 2)) - (4 * A_COF))) / 2
        t_2 = (c_sqr + math.sqrt((pow(c_sqr, 2)) - (4 * A_COF))) / 2
​
        t_1 = round(math.sqrt(t_1), 3)
        t_2 = round(math.sqrt(t_2), 3)
    
    except ValueError:
        return "Does not exist"
​
    return [t_1, t_2]

