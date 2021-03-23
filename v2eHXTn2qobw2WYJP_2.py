"""


Create a function that takes a list representation of a Minesweeper board, and
returns another board where the value of each cell is the amount of its
neighbouring mines.

### Examples

The input may look like this:

    [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 1, 0, 0]
    ]

The `0` represents an **empty space** . The `1` represents a **mine**.

You will have to replace each **mine** with a `9` and each **empty space**
with the number of adjacent mines, the output will look like this:

    [
      [1, 9, 2, 1],
      [2, 3, 9, 2],
      [3, 9, 4, 9],
      [9, 9, 3, 1]
    ]

### Notes

  * Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.
  * A wikipedia page explaining how Minesweeper works is available in the **Resources** tab.

"""

def minesweeper_numbers(board):
  height = len(board)
​
  for y in range(height):
      for x in range(height):
          el = board[y][x]
          if el==1:
              board[y][x]=9
​
  for y in range(height):
      for x in range(height):
          el = board[y][x]
          if el!=9:
              if x>0:
                  if board[y][x-1]==9:     #check left
                      board[y][x]+=1     
              if x<height-1:
                  if board[y][x+1]==9:     #check right
                      board[y][x]+=1   
              if y>0:
                  if board[y-1][x]==9:     #check up
                      board[y][x]+=1     
              if y<height-1:
                  if board[y+1][x]==9:     #check down
                      board[y][x]+=1
              if x>0 and y>0:
                  if board[y-1][x-1]==9:   #check north-west
                      board[y][x]+=1
              if x<height-1 and y>0:
                  if board[y-1][x+1]==9:   #check north-east
                      board[y][x]+=1
              if x>0 and y<height-1:
                  if board[y+1][x-1]==9:   #check south-west
                      board[y][x]+=1
              if x<height-1 and y<height-1:
                  if board[y+1][x+1]==9:   #check south-west
                      board[y][x]+=1
  return board

