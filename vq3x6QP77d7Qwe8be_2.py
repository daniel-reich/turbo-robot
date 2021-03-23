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

def has_odd_patch(lst, size):
    for ii in range(1+len(lst)-size):
        for jj in range(1+len(lst[0])-size):
            square = [row[jj:jj+size] for row in lst[ii:ii+size]]
            if square and all(num%2 for row in square for num in row):
                return True
def odd_square_patch(lst):
    for size in range(min(len(lst), len(lst[0])),0,-1):
        if has_odd_patch(lst, size):
            return size
    return 0

