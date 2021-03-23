"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
​
  board = []
  highest = 1
  for num in range(int(n/2)+1):
    row = []
    score = 1
    d = highest - 1
    for numb in range(n):
      row.append(str(score))
      if score < highest:
        score += 1
    
    for numb in range(1, 1+d):
      row[-numb] = str(0 + numb)
    board.append(int(''.join(row)))
    highest += 1
  
  if n%2!=0:
    return board + list(reversed(board[:-1]))
  else:
    return board + list(reversed(board[:-2]))

