"""


Create a function that takes the name of a chess piece, its position and a
target position. The function should return `True` if the piece can move to
the target and `False` if it can't.

The possible inputs are "Pawn", "Knight", "Bishop", "Rook", "Queen" and
"King".

### Examples

    can_move("Rook", "A8", "H8") ➞ True
    
    can_move("Bishop", "A7", "G1") ➞ True
    
    can_move("Queen", "C4", "D6") ➞ False

### Notes

  * Do not include pawn capture moves and en passant.
  * Do not include castling.
  * Remember to include pawns' two-square move on the second rank!
  * Look for patterns in the movement of the pieces.

"""

def can_move(piece, current, target):
  options = []
  row = current[0]
  col = current[1]
  if piece == 'Pawn':
    options.append(row + change_val(col,1))
    if col == '2':
      options.append(row+change_val(col,2))
  if piece == 'Knight':
    for i in range(-2, 3):
      if i == 0:
        continue
      options.append(change_val(row,i)+change_val(col,3-abs(i)))
      options.append(change_val(row,i)+change_val(col,abs(i)-3))
  if piece in ['Bishop', 'Queen']:
    for i in range(1,9):
      options.append(change_val(row,i)+change_val(col,i))
      options.append(change_val(row,-i)+change_val(col,-i))
      options.append(change_val(row,-i)+change_val(col,i))
      options.append(change_val(row,i)+change_val(col,-i))
  if piece in ['Rook', 'Queen']:
    for i in range(1,9):
      options.append(change_val(row,i)+col)
      options.append(change_val(row,-i)+col)
      options.append(row+change_val(col,i))
      options.append(row+change_val(col,-i))
  if piece == 'King':
    for i in range(-1,2):
      for j in range(-1,2):
        if i!=0 or j!=0:
          options.append(change_val(row,i)+change_val(col,j))
  return (target in options)
    
def change_val(val, change_size):
  return chr(ord(val)+change_size)

