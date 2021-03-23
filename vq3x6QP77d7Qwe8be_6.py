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
  max_size = 0
  for row in range(len(lst)):
    for col in range(len(lst[row])):
      if lst[row][col]%2 == 1:
        all_odd = True
        size = 1
        while all_odd:
          if row+size >= len(lst):
            all_odd = False
          else:
            if col+size >= len(lst[row+size]):
              all_odd = False
            else:
              i = col
              while i <= col+size and all_odd:
                if lst[row+size][i]%2 != 1:
                  all_odd = False
                i += 1
          i = row
          while i <= row+size-1 and all_odd:
            if col+size >= len(lst[i]):
              all_odd = False
            elif lst[i][col+size]%2 != 1:
              all_odd = False
            i += 1
          if all_odd:
            size += 1
        if size > max_size:
          max_size = size
  return max_size

