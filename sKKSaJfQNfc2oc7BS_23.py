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

def sle (list1):
    equation1 = list1[0]
    equation2 = list1[1]
    a , b , c = equation1[0]  , equation1[1]   , equation1[2]
    d , e , f = equation2[0]  , equation2[1]   , equation2[2]
    denom = a * e - b * d
    if  denom == 0:
        return False
    return (  int((c*e - b*f)/denom), int((a*f - c*d)/denom) )

