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
    size, r, w, h = 0, 0, len(lst[0]), len(lst)
    while r < h - size:
        c = 0
        while c < w - size:
            d = 0
            while r + d < h and c + d < w:
                ext = [(r+d,x) for x in range(c, c+d+1)] + [(y,c+d) for y in range(r,r+d)]
                if not all(lst[i][j]%2 for i,j in ext):
                    break
                d += 1
                if d > size:
                    size = d
            c += 1
        r += 1
    return size

