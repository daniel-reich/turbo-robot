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

def sle(eq):
    # eq in form a*x + b*y = c
    eq1 = eq[0]
    eq2 = eq[1]
    
    # Make a1 and a2 the same but opposite values
    a1, a2 = eq1[0], eq2[0]
    
    # If both a1 and a2 are positive, make eq2 negative 
    if a1 > 0 and a2 > 0:
        eq2 = list(map(lambda a: a*(-1), eq2))
    
    eq1 = list(map(lambda a: a*a2, eq1))
    eq2 = list(map(lambda a: a*a1, eq2))
    
    # Add equations together, cancelling x out
    eq_sum = [n1 + n2 for n1,n2 in zip(eq1, eq2)]
    
    # Calculate x and y
    try:
        y = eq_sum[2]//eq_sum[1]
        x = (eq1[2] - eq1[1]*y)//eq1[0]
    except:
        return False
    return (x, y)

