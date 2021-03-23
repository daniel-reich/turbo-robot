"""


Write a function that returns `True` if the knights are placed on a chessboard
such that **no knight can capture another knight**. Here, `0`s represent empty
squares and `1`s represent knights.

### Examples

    cannot_capture([
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 0]
    ]) ➞ True
    
    cannot_capture([
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1, 0, 1]
    ]) ➞ False

### Notes

  * Knights can be present in any of the 64 squares.
  * No other pieces except knights exist.

"""

def cannot_capture(lst):
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if lst[y][x]==1:
                s = capturable(y,x,lst)
                for i in s:
                    if lst[i[1]][i[0]] == 1:
                        return False
    return True
​
def capturable(y,x,lst):
    indices = [[x+2,y+1],[x+2,y-1],[x+1,y+2],[x+1,y-2],[x-2,y+1],[x-2,y-1],[x-1,y+2],[x-1,y-2]]
    res = []
    for i in indices:
        if i[0]>=0 and i[1]>=0:
            try:
                lst[i[0]][i[1]]
                res+=[[i[0],i[1]]]
            except IndexError:
                continue
    return res

