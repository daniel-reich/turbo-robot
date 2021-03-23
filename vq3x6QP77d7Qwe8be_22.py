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
  lst = [[lst[i][j] % 2 for j in range(0,len(lst[0]))] for i in range(0,len(lst))]
  if not lst:
    return 0
  elif len(lst) == 1:
    return 1 if 1 in lst[0] else 0
  else:
    size = min(len(lst),len(lst[0]))
    while True:
      for i in range(0,len(lst)-size+1):
        for j in range(0,len(lst[0])-size+1):
          if lst[i][j] == 1:
            if all(list(map(lambda x: not 0 in lst[x][j:j+size],range(i,i+size)))):
              return size
      size -= 1

