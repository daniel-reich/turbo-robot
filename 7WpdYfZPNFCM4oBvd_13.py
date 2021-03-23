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

def is_magic(square):
    if len(square) == 0:
        return True
    import numpy as np
    square = np.array(square)
    if np.min(square) != 1:
        return False
    diag_sum = np.trace(square)
    diag_sum_ = np.trace(square[:, ::-1])
    if diag_sum != diag_sum:
        return False
    hor_sum = np.sum(square, axis=0)
    if (diag_sum == hor_sum).all() == False:
        return False
    ver_sum = np.sum(square, axis=1)
    if (diag_sum == ver_sum).all() == False:
        return False
    return True
