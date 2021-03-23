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
  for y in range(len(field)):
    for x in range(len(field[y])):
      if not watered(field,y,x):
        return False
  return True
  
def watered(lst,y,x):
  if lst[y][x] == 'w':
    return True
  if y>0:
    if lst[y-1][x] == 'w':
      return True
    if x>0 and lst[y-1][x-1] == 'w':
      return True
    if x<len(lst[0])-1 and lst[y-1][x+1] == 'w':
      return True
  if y<len(lst)-1:
    if lst[y+1][x] == 'w':
      return True
    if x>0 and lst[y+1][x-1] == 'w':
      return True
    if x<len(lst[0])-1 and lst[y+1][x+1] == 'w':
      return True
  if x>0 and lst[y][x-1] == 'w':
    return True
  if x<len(lst[0])-1 and lst[y][x+1] == 'w':
    return True
  return False

