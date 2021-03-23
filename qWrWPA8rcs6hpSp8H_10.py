"""


Create a function that returns the determinant of a given square matrix.

### Examples

    determinant([[3]]) ➞ 3
    
    determinant([[1, 0], [5, 4]]) ➞ 4
    
    determinant([[3, 0], [2, 2]]) ➞ 6
    
    determinant([[4, 8, 6], [2, 4, 3], [6, 2, 1]]) ➞ 0

### Notes

All inputs are square integer matrices.

"""

from functools import reduce
​
def determinant(a):
    def b(m, i):
        if m % 2 and m > 1:
            return i if i < m-1 else m-2
        return m-1
​
    def permutations(m):
        nonlocal s, sign
        if m:
            for i in range(m):
                permutations(m-1)
                p[b(m, i)], p[m] = p[m], p[b(m, i)]
            permutations(m-1)
        else:
            s += sign*reduce(int.__mul__, (a[i][j] for i,j in enumerate(p)))
            sign = -sign 
    
    sign, s = 1, 0
    p = list(range(len(a)))
    permutations(len(a)-1)
    return s

