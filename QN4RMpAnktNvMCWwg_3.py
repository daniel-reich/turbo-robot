"""


An identity matrix is defined as a square matrix with **1s** running from the
top left of the square to the bottom right. The rest are **0s**. The identity
matrix has applications ranging from machine learning to the general theory of
relativity.

Create a function that takes an integer `n` and returns the identity matrix of
`n x n` dimensions. For this challenge, if the integer is negative, return the
mirror image of the identity matrix of `n x n` dimensions.. It does not matter
if the mirror image is left-right or top-bottom.

### Examples

    id_mtrx(2) ➞ [
      [1, 0],
      [0, 1]
    ]
    
    id_mtrx(-2) ➞ [
      [0, 1],
      [1, 0]
    ]
    
    id_mtrx(0) ➞ []

### Notes

Incompatible types passed as `n` should return the string `"Error"`.

"""

def id_mtrx(n):
  if not isinstance(n,int):
    return 'Error'
  mtx = [[1 if i==j else 0 for j in range(abs(n))] for i in range(abs(n))]
  if n < 0:
    mtx = [row[::-1] for row in mtx]
  return mtx

