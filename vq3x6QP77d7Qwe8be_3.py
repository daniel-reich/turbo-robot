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

def is_all_odd(sub):
    for i in range(len(sub)):
        for j in range(len(sub[0])):
            if sub[i][j]%2==0:
                return False
    return True
def odd_square_patch(lst):
    width, height, squares = len(lst[0]), len(lst), [0]
    for i in range(height):
        for j in range(width):
            if lst[i][j]%2 == 1:
                squares.append(1)
                for k in range(1, min([height-i, width-j])+1):
                    arr = [lst[l][j: j+k] for l in range(i, i+k)]
                    if is_all_odd(arr):
                        squares.append(k)
    return max(squares)

