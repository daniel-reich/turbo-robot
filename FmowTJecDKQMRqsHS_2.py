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
  field2 = []
  for r in range(len(field)):
    for c in range(len(field[0])):
      watered = False
      for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
          x = min(max(0, r+i), len(field)-1)
          y = min(max(0, c+j), len(field[0])-1)
          if field[x][y] == 'w':
            watered = True
      field2 += [watered]
  return all(field2)

