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

def isMagic(square):
  if not square:
    return True
  square1 = list(map(list,zip(*square)))
  chk = sum(square[0])
  if any(sum(square[i])!= chk or sum(square1[i])!=chk for i in range(len(square))):
    return False
  tot1,tot2,tot3 = 0,0,0
  for i in range(len(square)):
    tot1 += square[i][i]
    tot2 += square1[i][i]
    tot3 += sum(square[i])
  if tot3 != sum(range(1,len(square)**2+1)):
    return False
  if tot1 !=  chk or tot2 != chk:
    return False
  return True

