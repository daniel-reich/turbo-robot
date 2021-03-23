"""


Given a list containing three strings, representing the rows of an O's and X's
board from top to bottom, return the row and column position of the winning
move for X's. Return `False` if the game cannot be won.

### Examples

    x_and_o(board = [" | | ", " |X| ", "X| | "]) ➞  [1, 3]
    
    # Board becomes:
    #    |   |
    #    |X |
    # X |   |
    
    x_and_o(board = ["X|X|O", "O|X| ", "X|O| "]) ➞ [3, 3]
    
    # Board becomes:
    # X|X|O
    # O|X|
    # X|O|

### Notes

There is no 0 index for the row or column.

"""

def x_and_o(board):
  out=[]
  rows = [[1 if i=='X' else 0 if i=='O' else -1 for i in board[0].split('|')],
  [1 if i=='X' else 0 if i=='O' else -1 for i in board[1].split('|')],
  [1 if i=='X' else 0 if i=='O' else -1 for i in board[2].split('|')]]
  i=1
  for row in rows:
    if -1 in row and 1 in row and not 0 in row and sum(row) ==1:
      out=[i,row.index(-1)+1]
      break
    i+=1
  i=1
  for j in range (len(rows)):
    if -1 in [row[j] for row in rows] and 1 in [row[j] for row in rows] \
    and not 0 in [row[j] for row in rows] and sum([row[j] for row in rows]) ==1:
      out=[[row[j] for row in rows].index(-1)+1,i]
      break
    i+=1
    
  if (rows[0][0]+ rows[1][1]+ rows[2][2] ==1 and -1 in [rows[0][0],rows[1][1],rows[2][2]]):
    out = [[rows[0][0],rows[1][1],rows[2][2]].index(-1)+1,\
    [rows[0][0],rows[1][1],rows[2][2]].index(-1)+1]
  
  if (rows[0][2]+ rows[1][1]+ rows[2][0] ==1 and -1 in [rows[0][2],rows[1][1],rows[2][0]]): 
    if(-1 == rows[0][2]):
      out=[1,3]
    elif(-1 == rows[1][1]):
      out= [2,2]
    else:
      out = [3,1]
  
  if len(out) >0:
    return out
  else:
    return False

