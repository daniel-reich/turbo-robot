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
  d1 = None
  d2 = None
  numbers = None
  try:
    d1 = sum(list(map(lambda x: square[x][x],range(0,len(square)))))
    d2 = sum(list(map(lambda x: square[len(square)-1-x][x],range(0,len(square)))))
  except IndexError:
    pass
  try:
    numbers = [square[n // len(square)][n % len(square)] for n in range(0,pow(len(square),2))]
  except IndexError:
    pass
  def cols(j):
    return sum([square[i][j] for i in range(0,len(square))])
    
  if not square:
    return True
  elif min(list(map(lambda x: len(x),square))) != max(list(map(lambda x: len(x),square))):
    return False
  elif len(square) != len(square[0]):
    return False
  elif sorted(numbers) != list(range(1,pow(len(square),2)+1)):
    return False
  elif d1 != d2:
    return False
  elif any(list(map(lambda x: sum(x) != d1,square))):
    return False
  else:
    return all(list(map(lambda x: cols(x) == d1,range(0,len(square)))))

