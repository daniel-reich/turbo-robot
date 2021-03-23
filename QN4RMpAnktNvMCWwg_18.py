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
   
    empty = []
    empty_2 = []
    if isinstance(n,str):
        return "Error"
    if n > 0:
        for i in range(n):
            for j in range(n):
                if i == j:
                    empty_2.append(1)
                else:
                    empty_2.append(0)
        a = [empty_2[x:x+n] for x in range(0,len(empty_2),n)]
        return a
               
    if n < 0:
        for b in range(abs(n)):
            for c in range(abs(n)):
                if b == c:
                    empty.append(1)
                else:
                    empty.append(0)
        k = [empty[l:l+abs(n)] for l in range(0,len(empty),abs(n))]
        k.reverse()
        return k
    if n == 0:
        return 0

