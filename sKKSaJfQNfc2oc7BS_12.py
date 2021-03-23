"""


Given two simultaneous linear equations in this form: `a*x + b*y = c`, `d*x +
e*y = f`, devise a function that returns the values of `x` and `y` as `(x,
y)`. The numbers `a` through `f` are non-zero integers. If there is not a
unique solution or if there is no solution at all, return `False`. Input is
given as: `[[a, b, c], [d, e, f]]`. Solutions, if they exist, will be
integers.

### Examples

    sle([[3, 4, 19], [2, -1, 9]]) ➞ (5, 1)
    
    sle([[3, 2, -2], [2, 5, -5]]) ➞ (0, -1)
    
    sle([[4, -3, 18], [8, -6, 36]]) ➞ False
    
    sle([[2, 3, 13], [5, -1, 7]]) ➞ (2, 3)

### Notes

Can you do this without using numpy?

"""

def sle(m):
    la = m[0]
    lb = m[1]
​
    val = 0
    for val in range(1, 100):
        if((val / la[0]) == (val // la[0]) and
           (val / lb[0]) == (val // lb[0])):
            break
​
    laP = la[:]
    m = val / laP[0]
    laP[0] *= m
    laP[1] *= m
    laP[2] *= m
    
    lbP = lb[:]
    m = val / lbP[0]
    lbP[0] *= m
    lbP[1] *= m
    lbP[2] *= m
​
    if(abs(laP[1]) == abs(lbP[1])):
        return False
        
​
    #print(laP, " ", lbP)
​
    cy = laP[1] - lbP[1]
    c = laP[2] - lbP[2]
    y = c / cy
​
    x = (la[2] - (la[1] * y)) / la[0]
​
    #print(x, " ", y)
​
    return (x, y)

