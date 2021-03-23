"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

def spiral_transposition(lst):
    w, h = len(lst[0]), len(lst)
​
    is_blocked = lambda r, c, dr, dc: not(0<=r+dr<h and 0<=c+dc<w and lst[r+dr][c+dc] >= 0)
​
    r, c, dr, dc, res, done = 0, 0, 0, 1, [], False
    while True:
        res.append(lst[r][c])
        lst[r][c] = -1
        if is_blocked(r, c, dr, dc):
            dr, dc = dc, -dr
            if is_blocked(r, c, dr, dc):
                return res
        r,c = r+dr, c+dc

