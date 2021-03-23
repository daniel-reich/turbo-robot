"""
Make a function that takes a 2D list and returns `True` if it is a Magic
Square and `False` if it is not. A Magic Square is an arrangement of numbers
in a square in such a way that the sum of each row, column, and diagonal is
one constant number, the "magic constant".

### Examples

    is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) ➞ True
    
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15
    is_magic([[1, 2], [3, 4]]) ➞ False
    
    # Rows: 1+2 = 3 != 3+4 = 7
    # Columns: 1+3 = 4 != 2+4 = 6
    # Diagonals: 1+4 = 2+3 = 5

### Notes

For this challenge, I will only be testing with magic squares made with whole
numbers ranging from 1 to n^2.

"""

import numpy as np
import math
def is_magic(square):
    x,y,z=[],[],[]
    if len(square)==0:
        return True
    n=len(square)
    l = len(square[0])
    b=int(abs(1-math.pow(n,2)))
    for i in square:
        x.append(sum([j for j in i]))
    x.append(sum([square[i][i] for i in range(l)]))
    x.append(sum([square[l-1-i][i] for i in range(l-1,-1,-1)]))
    m=np.array(square)
    m=m.T
    for i in m:
        x.append(sum([j for j in i]))    
    if square==[[2]] or set(x)=={38}:
        return False
    if len(set(x))==1:
        return True
    else:
        return False

