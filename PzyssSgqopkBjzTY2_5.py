"""


A maze can be represented by a 2D matrix, where `0`s represent **walkeable**
areas, and `1`s represent walls. You start on the upper left corner and the
exit is on the most lower right cell.

Create a function that returns `true` if you can walk from one end of the maze
to the other. You can only move up, down, left and right. You **cannot move
diagonally**.

### Examples

    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0]
    ]) ➞ true
    
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 1, 1]
    ]) ➞ false
    
    # This maze only has dead ends!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1]
    ]) ➞ false
    
    # Exit only one block away, but unreachable!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 0]
    ]) ➞ true

### Notes

  * In a maze of size `m x n`, you enter at `[0, 0]` and exit at `[m-1, n-1]`.
  * There can be dead ends in a maze - one exit path is sufficient.

"""

def can_exit(test):
    ylen = test.__len__(); xlen = test[0].__len__() 
    if test[0][0] == 1 or test[ylen - 1][xlen - 1] == 1: return False
    endarrays = {'startarray': {'check': [[0, 0]], 'prev': [], 'final': []}, 'endarray': {'check': [[xlen - 1, ylen - 1]], 'prev': [], 'final': []}}
    for i in range(0, (ylen - 1) * (xlen - 1)):
        for endarray in endarrays:
            for array in endarrays[endarray]['check']:
                checkarray = [[array[0] - 1, array[1]], [array[0] + 1, array[1]], [array[0], array[1] - 1], [array[0], array[1] + 1]]
                for point in checkarray:
                    pointindex = checkarray.index(point)
                    if checkarray[pointindex][0] < 0 or checkarray[pointindex][1] < 0: continue
                    if checkarray[pointindex][0] > (xlen - 1) or checkarray[pointindex][1] > (ylen - 1): continue
                    if test[checkarray[pointindex][1]][checkarray[pointindex][0]] == 1: continue
                    if not point in endarrays[endarray]['prev']:
                        endarrays[endarray]['prev'].append(point); endarrays[endarray]['final'].append(point)
                        if endarray == 'startarray':
                            if point in endarrays['endarray']['final']:
                                return True
                        else:
                            if point in endarrays['startarray']['final']:
                                return True
            endarrays[endarray]['check'] = endarrays[endarray]['prev'].copy()
            endarrays[endarray]['prev'] = []   
    return False

