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

def where_is_waldo(A):
  # Find what the letter is 
  for lst in A:
    if len(set(lst)) != 1:
      for i in set(lst):
        if lst.count(i) == 1:
          letter = i 
  # Find where the letter is 
  for row in A:
    if letter in row:
      row_idx = A.index(row) + 1
  for i in A[row_idx - 1]:
    print(i)
    if i == letter:
      col_idx = A[row_idx - 1].index(i) + 1
​
  return [row_idx, col_idx]

