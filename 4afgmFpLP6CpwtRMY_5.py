"""


Write a **sudoku validator**. This function should return `True` if the 2-D
array represents a valid sudoku and `False` otherwise. To be a valid sudoku:

  1. Each row must have the digits from 1 to 9 exactly once.
  2. Each column must have the digits from 1 to 9 exactly once.
  3. Each 3x3 box must have the digits from 1 to 9 exactly once.

### Examples

    sudoku_validator([
      [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
      [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
      [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
      [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
      [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
      [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
      [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
      [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
      [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
    ]) ➞ True
    
    sudoku_validator([
      [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
      [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
      [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
      [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
      [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
      [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
      [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
      [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
      [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
    ]) ➞ False

### Notes

N/A

"""

def sudoku_validator(solution):
  valid = True
  # Validate squares
  for square in sudoku_get_squares(solution):
    if (not sudoku_group_valid(square)):
      valid = False
​
  # Validate the columns
  for column in sudoku_get_columns(solution):
    if (not sudoku_group_valid(column)):
      valid = False
​
  # Validate the rows
  for row in solution:
    if (not sudoku_group_valid(row)):
      valid = False
​
  return valid
​
def sudoku_group_valid(group):
  valid = True
  # Check the 1 - 9 values are unique
  for num in range(1, 10):
    if (group.count(num) > 1):
      valid = False
  return valid
​
def sudoku_get_columns(solution):
  columns = []
  for x in range(0, 9):
    column = []
    for y in range(0, 9):
      column.append(solution[y][x])
    columns.append(column)
  return columns
​
def sudoku_get_squares(solution):
  squares = []
  # Looking at the center item of each square and
  # pulling the square based on that
  for y in range(1, 8, 3):
    for x in range(1, 8, 3):
      square = []
      square.extend(solution[y - 1][x - 1 : x + 2])
      square.extend(solution[y]    [x - 1 : x + 2])
      square.extend(solution[y + 1][x - 1 : x + 2])
      squares.append(square)
  return squares

