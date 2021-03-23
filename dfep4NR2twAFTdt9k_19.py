"""


Create a function that multiplies two matricies (n x n each).

### Examples

    matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
    
    matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]
    
    matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

### Notes

Limit yourself to 2 x 2 matricies.

"""

def matrix_mult(m1, m2):
    a = m1[0][0] * m2[0][0] + m2[1][0] * m1[0][1]
    b = m1[0][0] * m2[0][1] + m2[1][1] * m1[0][1]
    c = m1[1][0] * m2[0][0] + m2[1][0] * m1[1][1]
    d = m1[1][0] * m2[0][1] + m2[1][1] * m1[1][1]
    return [[a,b],[c,d]]

