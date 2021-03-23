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
  flat_list = [x for y in lst for x in y]
  unique_row = 0
  unique_col = 0
  unique_char = ''
​
  for char in set(flat_list):
    if flat_list.count(char) == 1:
      unique_char = char
      break
​
  for row in range(len(lst)):
    if unique_char in lst[row]:
      unique_row = row
      break
​
  for col in range(len(lst[0])):
    if lst[unique_row][col] == unique_char:
      unique_col = col
      break
​
  return [unique_row + 1, unique_col + 1]

