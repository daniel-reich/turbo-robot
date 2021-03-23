"""


Your chess teacher wants to know if a bishop can reach a certain spot on the
board in the given amount of moves.

Given a starting square `start`, ending square `end` and the maximum number of
moves allowed `n`. Return `True` if the ending square can be reached from the
starting square within the given amount of moves. Keep in mind the chessboard
goes from a1 to h8 (8x8).

### Examples

    bishop("a1", "b4", 2) ➞ True
    
    bishop("a1", "b5", 5) ➞ False
    
    bishop("f1", "f1", 0) ➞ True

### Notes

  * Chessboard is always empty (only the bishop is there).
  * Bishop can move in any direction diagonally.
  * If the starting and ending square are the same, return `True` (even if the move is 0).
  * Square names will always be lowercase and valid.

"""

alph = 'abcdefgh'
import math
lst = []
for i in range(8):
    for a in range(8):
        lst.append(alph[a] + str(i + 1))
#print(lst)
​
refDict = {}
for a in lst:
    
    refDict[a] = ( alph.index(a[0]) , int(a[1]) )  
​
​
#Move towards
#Check distance
​
def getReachable(pos):
    out = []
    posX = refDict[pos][0]
    posY = refDict[pos][1]
    for key in refDict.keys():
        if key == pos:
            continue
        x = refDict[key][0]
        y = refDict[key][1]
        if (posX - x) == 0:
            continue
        slope = (posY - y) / (posX - x)
​
        if slope == 1 or slope == -1:
            out.append(key)
    return out
​
def closest(start, end):
    startX = refDict[start][0]
    startY = refDict[start][1]
    endX = refDict[end][0]
    endY = refDict[end][1]
    
    distances = {}
​
    for pos in getReachable(start):
        pX = refDict[pos][0]
        pY = refDict[pos][1]
        if pX == startX and pY == startY:
            return pos
        dist = math.sqrt( (pX - endX) ** 2 + (pY - endY) ** 2 )
        distances[pos] = dist
​
    for key in distances.keys():
        if distances[key] == min(distances.values()):
            #print(distances)
            return key
​
#Returns true if it forms a     #
                              # X #
                                #
def isImpossible(start, end):
    start = refDict[start]
    end = refDict[end]
​
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
​
    if startX == endX and abs(startY - endY) == 1:
        return True
    if startY == endY and abs(startX - endX) == 1:
        return True
    return False
​
def bishop(start, end, num):
  if start == end:
    return True
  close = closest(start, end)
  i = 0
  while i < num:
​
​
    if close == end:
      return True
    if isImpossible(close, end):
      return False
    else:
      close = closest(close, end)
    i = i + 1
  return False

