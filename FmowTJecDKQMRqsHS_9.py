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

import numpy as np
def crop_hydrated(field):
  field = np.array(field) == 'w'
  watered = 0 * field
  for i,j in np.ndindex(field.shape):
    if field[i,j]:
      for u,v in np.ndindex((3,3)):
        try: watered[i+u-1,j+v-1] = 1
        except: pass
  
  return np.sum(watered == 0) == 0

