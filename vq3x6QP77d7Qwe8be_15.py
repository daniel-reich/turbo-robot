"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst):
    row = len(lst); col = len(lst[0]); res = [[0]*col for i in range(row)]; max_res = 0
    for i in range(row):
        for j in range(col):
            if lst[i][j] % 2: lst[i][j] = 1
            else: lst[i][j] = 0
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 1: 
                res[i][j] = min(res[i][j-1], res[i-1][j-1], res[i-1][j]) + 1
                if res[i][j] > max_res: max_res = res[i][j]
    return max_res

