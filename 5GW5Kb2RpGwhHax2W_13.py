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
    n,idx = [],[]
    while len(lst) > 1:
        top = lst[0]
        bottom = lst[-1]
        left,right = [],[]
        for sub in lst[1:-1]:
            left.append(sub[0])
            right.append(sub[-1])
        spiral = top + right + bottom[::-1] + left[::-1]
        n += spiral
        del lst[0]
        del lst[-1]
        for sub in lst:
            del sub[-1]
            del sub[0]
    if lst:
        n += lst[0]
    return n

