"""


Create a function that multiplies two matricies (n x n each).

### Examples

    matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
    
    matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]
    
    matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

### Notes

Limit yourself to 2 x 2 matricies.

"""

def row(m, i):
    return m[i]
​
def col(m, i):
    res = []
    for j in range(len(m)):
        res.append(m[j][i])
    return res
​
def mult_entry(m1, m2, x, y):
    res = 0
    r = row(m1, x)
    c = col(m2, y)
    for i in range(len(m1[0])):
        res += r[i] * c[i]
    return res
​
def matrix_mult(m1,m2):
    m = len(m1)
    n = len(m1[0])
    res = [[0 for y in range(n)] for x in range(m)]
    for x in range(m):
        for y in range(n):
            res[x][y] = mult_entry(m1, m2, x, y)
    return res

