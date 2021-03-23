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

def list_validator(lst):
  for n in range(1,10):
    if n not in lst:
      return False
  return True
  
  
def sudoku_validator(x):
  orizontal = []
  for lst in x:
    orizontal = list_validator(lst)
    if orizontal != True:
      return False
  for n in range(0,9):
    vertical = []
    for lst in x:
      vertical.append(lst[n])
    if list_validator(vertical) != True:
      return False
      
  square_list = [0, 3, 6, 9]
  
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 0
      while m < 3:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False  
      
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 3
      while m < 6:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False
      
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 6
      while m < 9:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False
      
  return True

