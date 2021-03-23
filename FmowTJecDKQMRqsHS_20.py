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
    options_to_visit = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
​
    for row_idx in range(0, len(field)):
        for col_idx in range(0, len(field[row_idx])):
            if field[row_idx][col_idx] == "c":
                for x, y in options_to_visit:
                    if 0 <= row_idx+x < len(field) and 0 <= col_idx+y < len(field[row_idx]):
                        if field[row_idx+x][col_idx+y] == 'w':
                            break
                else:
                    return False
    else:
        return True

