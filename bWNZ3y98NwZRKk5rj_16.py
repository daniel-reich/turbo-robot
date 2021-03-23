"""


Create a function that returns a number which can block the player from
reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument
will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2,
bottomleft is 6, and bottomright is 8.

  * Create a function that takes two numbers `a`, `b` and returns another number.
  * This number should be the final one in a line to block the player from winning.

### Examples

    block_player(0, 3) ➞ 6
    
    block_player(0, 4) ➞ 8
    
    block_player(3, 5) ➞ 4

### Notes

The values given will always have two filled squares in a line.

"""

def block_player(a, b):
  if abs(b - a) % 3 == 0:
    step = 3
    colNum = b % 3
    possibilityList = range(colNum, (colNum+2*3)+1, step)
  elif b % 2 == 0 and a % 2 == 0:
    list1 = [0, 4, 8]
    list2 = [2, 4, 6]
    if a in list1 and b in list1:
      possibilityList = list1
    else:
      possibilityList = list2
  else:
    step = 1
    rowNum = b // 3
    possibilityList = range(rowNum*3, rowNum*3+3, step)
​
  return list(set(possibilityList) - set([a, b]))[0]

