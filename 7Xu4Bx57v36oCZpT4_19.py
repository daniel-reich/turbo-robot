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
  waldo = max(w for l in lst for w in l)
  col = [l for l in lst if waldo in l ]
  return [lst.index(col[0])+1,col[0].index(waldo)+1]

