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

def get_neighbours(r, c):
    return ((r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), 
            (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
​
def crop_hydrated(field):
    rows, cols = len(field), len(field[0])
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'c' and not any(field[i][j] == 'w' for i, j in get_neighbours(r, c) \
                if 0 <= i < rows and 0 <= j < cols):
                return False
    return True

