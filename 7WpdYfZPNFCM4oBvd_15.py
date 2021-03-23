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
    if not square:
        return True
    flat = [i for j in square for i in j]
    for i in range(1,max(flat)+1):
        if i not in flat:
            return False
    k = sum(square[0])
    tran = list(map(list,zip(*square)))
    row = [sum(i) == k for i in square]
    col = [sum(i) == k for i in tran]
    diag1 = [sum([square[i][i] for i in range(len(square))]) == k]
    diag2 = [sum([square[i][i] for i in range(len(square[::-1]))]) == k]
    return all(row + col + diag1 + diag2)

