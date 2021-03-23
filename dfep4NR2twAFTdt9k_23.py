"""


Create a function that multiplies two matricies (n x n each).

### Examples

    matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
    
    matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]
    
    matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

### Notes

Limit yourself to 2 x 2 matricies.

"""

def matrix_mult(m1,m2):
    ans= [[0,0],[0,0]]
    for i in range(2):
       for j in range(2):
           for k in range(2):
               ans[i][j] += m1[i][k] * m2[k][j]
    return ans

