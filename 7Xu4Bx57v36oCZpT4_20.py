"""


Return the coordinates (`[row, col]`) of the element that differs from the
rest.

### Examples

    where_is_waldo([
      ["A", "A", "A"],
      ["A", "A", "A"],
      ["A", "B", "A"]
    ]) ➞ [3, 2]
    
    where_is_waldo([
      ["c", "c", "c", "c"],
      ["c", "c", "c", "d"]
    ]) ➞ [2, 4]
    
    where_is_waldo([
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["P", "O", "O", "O"],
      ["O", "O", "O", "O"]
    ]) ➞ [5, 1]

### Notes

  * The given list will always be a square.
  * Rows and columns are 1-indexed ( **not zero-indexed** ).

"""

def where_is_waldo(lst):
  rest, w_row, w_col = '', 0, 0
  for idx, row in enumerate(lst):
    if len(set(row)) == 1:
      rest = row[0]
    if len(set(row)) == 2:
      w_row = idx
    if rest and w_row:
      break
  for i in range(len(lst[w_row])):
    if lst[w_row][i] != rest:
      w_col = i
      break
  return [w_row + 1, w_col + 1]

