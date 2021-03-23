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
​
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == "c":
                field[i][j] = sum([1 for u in range(i-1, i+2) for v in range(j-1, j+2)\
                                if 0 <= u < len(field) and 0 <= v < len(field[i]) and field[u][v] == "w"])
​
    field = [x for each in field for x in each]
    return True if not 0 in field else False

