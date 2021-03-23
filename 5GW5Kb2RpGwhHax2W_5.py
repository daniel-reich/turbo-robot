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
  l = []
  l.extend(lst[0])
  col1 = []
  for i in range(1,len(lst)-1):
    col1.append(lst[i][-1])
  l.extend(col1)
  l.extend(lst[-1][::-1])
  col2 = []
  for i in range(1,len(lst)-1):
    col2.append(lst[i][0])
  col2.reverse()
  l.extend(col2)
  if len(lst) > 2 and len(lst[1])>2:
    new = [r[1:-1] for r in lst[1:-1]]
    l1 = spiral_transposition(new)
    if len(lst) == 3:
      l1 = l1[:-1]
    l.extend(l1)
  return l

