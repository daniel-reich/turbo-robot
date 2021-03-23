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

def sudoku_validator(x):
​
  def checker(lst):
    return len(set(lst))==len(lst)
  
  #check the rows
  rowChk = []
  rowChk = [checker(n) for n in x]
  
  #check the columns
  colChk = []
  for c in range(9):
    col = [row[c] for row in x]
    colChk.append(checker(col))
  
  #check the 3X3 boxes
  boxChk = []
  for j in range(0,9,3):
    for i in range(0,9,3):
      box = [x[r][c] for c in range(0+j,3+j) for r in range(0+i,3+i)]
      boxChk.append(checker(box))
  
  
  return all(rowChk)==True and all(colChk)==True and all(boxChk)==True

