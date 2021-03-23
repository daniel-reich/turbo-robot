"""


This challenge involves finding words in an 8x8 grid. Given a string of 64
`letters` and a list of `words` to find, convert the string to an 8x8 list,
and return `True` if _all_ words in the string can be found in the list.
Return `False` otherwise. Words can be read in any direction ( _horizontally_
, _vertically_ or _diagonally_ ).

### Example

    letters = "PSUWHATSLPACKAGENYOLRDVLFINGEZBMIREHQNJOATBVGYESJDUWUESTPSTICKEY"
    words = ["stick", "most", "key", "vein", "yes", "package", "tube", "target", "elm", "spy"]

This would give the list below:

    [
      ["P", "S", "U", "W", "H", "A", "T", "S"],
      ["L", "P", "A", "C", "K", "A", "G", "E"],
      ["N", "Y", "O", "L", "R", "D", "V", "L"],
      ["F", "I", "N", "G", "E", "Z", "B", "M"],
      ["I", "R", "E", "H", "Q", "N", "J", "O"],
      ["A", "T", "B", "V", "G", "Y", "E", "S"],
      ["J", "D", "U", "W", "U", "E", "S", "T"],
      ["P", "S", "T", "I", "C", "K", "E", "Y"]
    ]

You would return `True` as all words can be found:

    [
      ["_", "S", "_", "_", "_", "_", "T", "_"],
      ["_", "P", "A", "C", "K", "A", "G", "E"],
      ["N", "Y", "_", "_", "R", "_", "_", "L"],
      ["_", "I", "_", "G", "_", "_", "_", "M"],
      ["_", "_", "E", "_", "_", "_", "_", "O"],
      ["_", "T", "B", "V", "_", "Y", "E", "S"],
      ["_", "_", "U", "_", "_", "E", "_", "T"],
      ["_", "S", "T", "I", "C", "K", "_", "_"]
    ]

### Notes

Words must be contained inside the grid, without wrapping over columns/rows.

"""

def findStartLetter(letter,grid):
    result = list()
    for i,row in enumerate(grid):
        for j,l in enumerate(row):
            if letter == l:
                result.append((i,j))
    return result
def findStringWords(startPos,length,grid):
    result = list()
    #up
    if startPos[0] - (length-1)>= 0:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]]
            word = word + nextLetter.lower()
        result.append(word)
    #down
    if startPos[0] + (length-1)<= 7:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]]
            word = word + nextLetter.lower()
        result.append(word)
    #right
    if startPos[1] + (length-1)<= 7:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
    #left
    if startPos[1] - (length-1)>= 0:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
    
     #up right
    if (startPos[0] - (length-1)>= 0) & (startPos[1] + (length-1)<= 7) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
    #down right
    if (startPos[0] + (length-1)<= 7) & (startPos[1] + (length-1)<= 7) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
        
    #up left
    if (startPos[0] - (length-1)>= 0) & (startPos[1] - (length-1)>= 0) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
        
    #down left
    if (startPos[0] + (length-1)<= 7) & (startPos[1] - (length-1)>= 0) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
​
    
    return result
​
def findWord(word,grid):
    pos = findStartLetter(word[0].upper(),grid)
    lst = list()
    for i in pos:
        lst.extend(findStringWords(i,len(word),grid))
    if word in lst:
        return True
    else:
        return False
​
def findWords(words,grid):
    for word in words:
        if findWord(word,grid):
            continue
        else:
            return False
    return True 
​
def makeGrid(letters):
    lst = list()
    for i in range(0,8):
        row = list()
        for j in range(0,8):
            row.append(letters[i*8 + j])
        lst.append(row)
    return lst
​
def word_search(letters, words):
    grid = makeGrid(letters)
    return findWords(words,grid)

