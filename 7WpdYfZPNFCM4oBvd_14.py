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
    ln = len(square)
    for r in square:
        if len(r) != ln:
            return False
    big = ln**2
    for i in range(ln):
        for j in range(ln):
            if square[i][j] > big:
                return False
    los = []
    los += [sum(r) for r in square]
    los += [sum(r) for r in map(list, zip(*square))]
    d1 = 0
    for i in range(ln):
        d1 += square[i][i]
    los.append(d1)
    d2 = 0
    for i in range(ln-1,-1,-1):
        d2 += square[i][i]
    los.append(d2)
    return len(set(los)) == 1

