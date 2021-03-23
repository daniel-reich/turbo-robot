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

def width_height(array):
    h = len(array)
    w = len(array[0])
    return w,h
​
def spiral_transposition(array, rimx=0, rimy=0):
    w, h= width_height(array)
    max_rings = min(w, h)//2
    ring = list()
    ring += [array[rimy][x] for x in range(rimx,w-rimx)]
    ring += [array[y][w-1-rimx] for y in range(rimy+1,h-rimy)]
    ring += [array[h-1-rimy][x] for x in range(w-2-rimx, rimx-1, -1)]
    ring += [array[y][rimx] for y in range(h-2-rimy, rimy, -1)]
    if rimx == max_rings or rimy == max_rings or (max_rings == 1 and (w==2 or h==2)):
        return ring
    else:
        return ring + spiral_transposition(array, rimx+1, rimy+1)

