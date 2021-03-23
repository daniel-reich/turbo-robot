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
  i = 0
  j = 1
  a1 = m1[i][i]
  a2 = m1[i][j]
  a3 = m1[j][i]
  a4 = m1[j][j]
​
  b1 = m2[i][i]
  b2 = m2[i][j]
  b3 = m2[j][i]
  b4 = m2[j][j]
​
  return [[a1*b1 + a2*b3, a1*b2 + a2 * b4],
  [a3*b1 + a4*b3, a3*b2 + a4*b4]]

