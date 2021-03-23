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
    watered_indexes = []
​
    # Create empty sets that correspond to field rows
    for i in range(len(field)):
        watered_indexes.append(set())
​
    for row in range(len(field)):
        for col in range(len(field[row])):
            cell = field[row][col]
            if cell == "w":
                # Then add all surrounding cell indexes to corresponding watered sets
                for i in range(row - 1, row + 2):
                    if i < 0 or i > len(field) - 1:
                        # Out of field's row's bounds
                        continue
                    for j in range(col - 1, col + 2):
                        if j < 0 or j > len(field[i]) - 1:
                            # Out of field's row's bounds
                            continue
                        watered_indexes[i].add(j)
​
    for i in range(len(field)):
        row_size = len(field[i])
        row_cells_watered = len(watered_indexes[i])
        if row_cells_watered < row_size:
            return False
    return True

