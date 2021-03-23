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
  rows, cols =  (-1,len(lst)), (-1,len(lst[0]))
  r, c = 0, 0
  track, res = set(), []
  direct = 1
​
  while len(res) < rows[1]*cols[1]:
    rn, cn = r, c
    if (r, c) not in track:
      res.append(lst[r][c])
      track.add((r,c))
​
    if direct == 1: cn += 1
    elif direct == 2: rn += 1
    elif direct == 3: cn -= 1
    else: rn -= 1
​
    if rn in rows or cn in cols or (rn, cn) in track:
      direct = direct+1 if direct < 4 else 1
    else:
      r, c = rn, cn
  return res

