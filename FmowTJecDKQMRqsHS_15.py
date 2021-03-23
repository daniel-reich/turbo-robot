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
  dict={}
  i=0
  while i<len(field):
    j=0
    while j<len(field[0]):
      if field[i][j]=="w":
        dict[(i-1,j-1)]=True
        dict[(i-1,j)]=True
        dict[(i-1,j+1)]=True
        dict[(i,j-1)]=True
        dict[(i,j+1)]=True
        dict[(i+1,j-1)]=True
        dict[(i+1,j)]=True
        dict[(i+1,j+1)]=True
      j+=1
    i+=1
  i=0
  while i<len(field):
    j=0
    while j<len(field[0]):
      if field[i][j]=="c":
        if not dict.get((i,j),False):
          return False
      j+=1
    i+=1
  return True

