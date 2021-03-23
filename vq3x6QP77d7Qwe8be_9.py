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
    max_width = min(len(lst), len(lst[0]))
    rlst = list(map(lambda r: list(map(lambda e: e%2, r)), lst))
    for width in range(max_width+1,0,-1):
        for i in range(len(lst)-width+1):
            for j in range(len(lst[0])-width+1):
                if all(map(lambda x: x == 1, [rlst[p][q] for p in range(i,i+width) for q in range(j,j+width)])):
                    return width
    return 0

