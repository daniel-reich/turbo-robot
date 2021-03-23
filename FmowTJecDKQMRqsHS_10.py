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
    for a in range(len(field)):
        for b in range(len(field[0])):
            if field[a][b] == "w":
                for c in range(-1, 2):
                    for d in range(-1, 2):
                        if 0 <= a + c < len(field) and 0 <= b + d < len(field[0]) and field[a + c][b + d] != "w":
                            field[a + c][b + d] = "#"
    return not any('c' in sublist for sublist in field)

