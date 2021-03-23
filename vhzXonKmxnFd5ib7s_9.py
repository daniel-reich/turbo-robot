"""


Create a function that multiplies two matrices (n x m) and (p x q) and
returns:

  * `"invalid"` if the matrices are not multiplicable (i.e. if m is not equal to p).
  * The multiplication matrix (n x q) otherwise.

### Examples

    matrix_multiply([[1, 2]], [[3], [4]]) ➞ [[11]]
    
    matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]) ➞ "invalid"
    
    matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

### Notes

This challenge is a generalized version of [Matrix
Multiplication](https://edabit.com/challenge/dfep4NR2twAFTdt9k).

"""

def matrix_multiply(a, b):
    n, m, p, q, res = len(a), len(a[0]), len(b), len(b[0]), []
    if m != p:
        return 'invalid'
    for i in range(n):
        res.append(q * [0])
    for i in range(n):
        for j in range(q):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(m))
    return res

