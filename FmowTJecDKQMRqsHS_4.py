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
    w_list = []
​
    y_size = len(field)
    x_size = len(field[0])
​
    hydrated_ind = [[1 for _ in range(x_size)] for _ in range(y_size)]
​
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col == 'w':
                w_list.append([x, y])
​
​
    for coord in w_list:
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                if x >= 0 and x <= x_size - 1 and y >= 0 and y <= y_size - 1:
                    hydrated_ind[y][x] = 0
​
    return not bool(sum([sum(l) for l in hydrated_ind]))

