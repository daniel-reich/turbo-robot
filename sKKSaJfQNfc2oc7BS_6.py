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

def sle(nested_list):
    A = [nested_list[0][:2], nested_list[1][:2]]
    b = [nested_list[0][2], nested_list[1][2]]
    x = [0, 0]
    def det(matrix):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if det(A) == 0:
        return False
    else:
        x[0] = int((b[0] * A[1][1] - A[0][1] * b[1]) / (A[0][0] * A[1][1] - A[0][1] * A[1][0]))
        x[1] = int((b[1] * A[0][0] - A[1][0] * b[0]) / (A[0][0] * A[1][1] - A[1][0] * A[0][1]))
        return tuple(x)

