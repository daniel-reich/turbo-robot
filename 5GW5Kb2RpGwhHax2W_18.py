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
    minrow, mincol = 0, 0,
    maxrow, maxcol = len(lst)-1, len(lst[0])-1
    step, lout, stepmax = 0, [], (maxrow+1)*(maxcol+1)
    while step < stepmax:
        for y in range(mincol, maxcol+1):
            lout.append(lst[minrow][y])
            step += 1
        minrow += 1
        for x in range(minrow, maxrow+1):
            lout.append(lst[x][maxcol])
            step += 1
        maxcol -= 1
        for y in range(maxcol, mincol-1, -1):
            lout.append(lst[maxrow][y])
            step += 1
        maxrow -= 1
        for x in range(maxrow, minrow-1, -1):
            lout.append(lst[x][mincol])
            step+=1
        mincol += 1
    return lout

