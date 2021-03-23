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
    m = len(lst)
    n = len(lst[0])
    r = min(m,n)
    for s in range(r,0,-1):
        for i in range(m-s+1):
            for j in range(n-s+1):
                count = 0
                for k1 in range(s):
                    for k2 in range(s):
                        if lst[i+k1][j+k2]%2 == 1:
                            count +=1
                if count == s*s:
                    return s
    return 0

