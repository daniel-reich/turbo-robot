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

def is_magic(s):
    n = len(s)
    if n == 0:
        return True
    n_max = n * n
    s_row = set()
    for row in s:
        if max(row) <= n_max and min(row) >= 1:
            s_row.add(sum(row))
        else:
            return False
    if len(s_row) != 1:
        return False
    m_num = s_row.pop()
    for col in zip(*s):
        if max(col) > n_max or min(col) < 1 or sum(col) != m_num:
            return False
    s1 = s2 = 0
    for i in range(n):
        s1 += s[i][i]
        s2 += s[i][n - 1 - i]
    return s1 == m_num and s2 == m_num

