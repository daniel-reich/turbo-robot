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
    rows, cols = len(field), len(field[0])
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'c':
                found_water = False
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (not (i == j == 0) and
                                0 <= r + i < rows and 0 <= c + j < cols
                                and field[r + i][c + j] == 'w'):
                            found_water = True
                            break
                    if found_water:
                        break
                if not found_water:
                    return False
    return True

