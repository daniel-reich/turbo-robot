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

def get_tile(current_row_index, current_column_index, x, y, field):
  height = len(field)
  width = len(field[0])
  new_row_index = current_row_index + y
  new_column_index = current_column_index + x
  if new_row_index < 0 or new_row_index >= height:
    return ''
  elif new_column_index < 0 or new_column_index >= width:
    return ''
  return field[new_row_index][new_column_index]
​
def is_hydrated(tile_value, row_index, column_index, field):
  if tile_value == 'w':
    return True
  else:
    string = ''
    string += get_tile(row_index, column_index, -1, -1, field)
    string += get_tile(row_index, column_index, 0, -1, field)
    string += get_tile(row_index, column_index, +1, -1, field)
    string += get_tile(row_index, column_index, -1, 0, field)
    string += get_tile(row_index, column_index, +1, 0, field)
    string += get_tile(row_index, column_index, -1, +1, field)
    string += get_tile(row_index, column_index, 0, +1, field)
    string += get_tile(row_index, column_index, +1, +1, field)
    return 'w' in string
​
def crop_hydrated(field):
  for row_index, field_row in enumerate(field):
    for column_index, tile_value in enumerate(field_row):
      if not is_hydrated(tile_value, row_index, column_index, field):
        return False
  return True

