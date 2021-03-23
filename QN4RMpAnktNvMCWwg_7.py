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
    if not isinstance(n, int):
        return "Error"
    counter = 0
    counter2 = 0
    scaling = 1
    if n < 0:
        scaling = -1
        counter2 = -1
        n = abs(n)
    list = [[0 for j in range(n)] for i in range(n)]
​
    for i in range(n):
        list[counter][counter2] = 1
        counter += 1
        counter2 += scaling
    return list

