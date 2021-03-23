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
  if isinstance(n, str):
    return "Error"
  
  matrix = []
  abs_n = abs(n)
  
  for idx in range(abs_n):
    inner_matrix = []
    for id in range(abs_n):
      if idx == id:
        inner_matrix.append(1)
      else:
        inner_matrix.append(0)
    if n > 0:
      matrix.append(inner_matrix)
    if n < 0:
      index = len(inner_matrix) - 1
      reverse_matrix = []
      while index >= 0:
        reverse_matrix.append(inner_matrix[index])
        index -= 1
      matrix.append(reverse_matrix)
      
  return matrix

