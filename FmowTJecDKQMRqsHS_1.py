"""


You're given a 2D list / matrix of a crop field. Each crop needs a water
source. Each water source hydrates the 8 tiles around it. With `"w"`
representing a water source, and `"c"` representing a crop, is every crop
hydrated?

### Examples

    crop_hydrated([
      [ "w", "c" ],
      [ "w", "c" ],
      [ "c", "c" ]
    ]) ➞ True
    
    crop_hydrated([
      [ "c", "c", "c" ]
    ]) ➞ False
    # There isn"t even a water source.
    
    crop_hydrated([
      [ "c", "c", "c", "c" ],
      [ "w", "c", "c", "c" ],
      [ "c", "c", "c", "c" ],
      [ "c", "w", "c", "c" ]
    ]) ➞ False

### Notes

`"w"` on its own should return `True`, and `"c"` on its own should return
`False`.

"""

def crop_hydrated(field):
    '''
    Returns True if any crops in field are neighbours of a water source, as
    explained in the instructions, otherwise False
    '''
    height, width = len(field), len(field[0])
    neighbours = lambda r,c: [field[i][j] for i in range(max(0,r-1),min(r+2, height))\
                              for j in range(max(0,c-1),min(c+2,width)) \
                              if not (i==r and j==c)]
​
    return all(['w' in neighbours(i,j) for i in range(height) \
                for j in range(width) if field[i][j] == 'c'])

