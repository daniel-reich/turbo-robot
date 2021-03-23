"""
Make a function that takes a 2D list and returns `True` if it is a Magic
Square and `False` if it is not. A Magic Square is an arrangement of numbers
in a square in such a way that the sum of each row, column, and diagonal is
one constant number, the "magic constant".

### Examples

    is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) ➞ True
    
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15
    is_magic([[1, 2], [3, 4]]) ➞ False
    
    # Rows: 1+2 = 3 != 3+4 = 7
    # Columns: 1+3 = 4 != 2+4 = 6
    # Diagonals: 1+4 = 2+3 = 5

### Notes

For this challenge, I will only be testing with magic squares made with whole
numbers ranging from 1 to n^2.

"""

def is_magic(square):
  size = len(square)
  magicNum =  (size**3 + size)/2
  for row in square:
      if sum(row) != magicNum or len(row) != size:
          return False  
  for col in range(size):
      column = [square[row][col] for row in range(size)]
      if sum(column) != magicNum:
          return False
  if sum([square[i][i] for i in range(size)]) != magicNum:
      return False
  if sum([square[i][(size-1)-i] for i in range(size)]) != magicNum:
      return False
  return True

