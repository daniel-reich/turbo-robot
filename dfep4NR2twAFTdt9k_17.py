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
  a=m1[0][0]
  b=m1[0][1]
  c=m1[1][0]
  d=m1[1][1]
  e=m2[0][0]
  f=m2[0][1]
  g=m2[1][0]
  h=m2[1][1]
  top_left=(a*e)+(b*g)
  top_right=(a*f)+(b*h)
  bottom_left=(c*e)+(d*g)
  bottom_right=(c*f)+(d*h)
  return [[top_left,top_right],[bottom_left,bottom_right]]

