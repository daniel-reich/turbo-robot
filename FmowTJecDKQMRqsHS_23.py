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
  for i in range(len(field)):
    for j in range(len(field[i])):
      if field[i][j] != 'w':
        c = 0
        adj = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        for x, y in adj:
          try:
            if i+x > -1 and j+y > -1:
              if field[i+x][j+y] == 'w':
                c += 1
                break
          except:
            pass
        if not c:
          return False
  return True

