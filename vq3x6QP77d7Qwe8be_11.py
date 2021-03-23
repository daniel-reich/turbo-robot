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
    for i in range(1,len(lst)+2):
        if not has_patch(lst, i):
            return i - 1
​
​
def has_patch(lst, n):
    if n>len(lst) or n>len(lst[0]):
        return False
    for i in range(len(lst)-n+1):
        for j in range(len(lst[0])-n+1):
            if is_odd([[l for l in k[j:j+n]]for k in lst[i:i+n]]):
                return True
    return False
def is_odd(lst):
    for i in lst:
        for j in i:
            if j % 2 != 1:
                return False
    return True

