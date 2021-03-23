"""


Write a function that takes in two floating-point numbers `s` and `p` and
returns a tuple of two floating-point numbers `(x, y)`, where _x_ \+ _y_ = _s_
and _x_ * _y_ = _p_. Round _x_ and _y_ to three decimal places.

If there are multiple solutions, return the solution with the lesser _x_ (or
lesser _y_ , if the _x_ values are equal).

Imaginary/complex number solutions are not allowed. If no real-valued
solutions exist, return `None`.

### Examples

    sum_and_product(2, -15) ➞ (-3.0, 5.0)
    
    sum_and_product(144, 144) ➞ (1.007, 142.993)
    
    sum_and_product(-42.7, 144.5) ➞ (-38.994, -3.706)
    
    sum_and_product(10, 30) ➞ None

### Notes

To solve this problem, consider setting up a system of two equations and
solving for x and y.

"""

def sum_and_product(s, p):
    if s**2 - 4 * p < 0:
        return None
    y1 = round((s + (s**2 - 4 * p)**.5)/2,3)
    y2 = round((s - (s**2 - 4 * p)**.5)/2,3)
    x1 = round(s - y1,3)
    x2 = round(s - y2,3)
​
    if x1 < x2:
        return (x1,y1)
    if x2 < x1:
        return (x2,y2)
    if y1 < y2:
        return (x1,y1)
    else:
        return (x2,y2)

