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

def check(grid,row,col,word,index=0,dirrow=0,dircol=0):
  if row >= 8 or col >= 8 or index >= len(word):
    return False
  else:
    if grid[row][col] != word[index]:
      return False
    else:
      if index == len(word)-1:
        return True
      elif dirrow == 0 and dircol == 0:
        return check(grid,row-1,col-1,word,index+1,-1,-1) or check(grid,row-1,col,word,index+1,-1,0) or check(grid,row-1,col+1,word,index+1,-1,1) or check(grid,row,col-1,word,index+1,0,-1) or check(grid,row,col+1,word,index+1,0,1) or check(grid,row+1,col-1,word,index+1,1,-1) or check(grid,row+1,col,word,index+1,1,0) or check(grid,row+1,col+1,word,index+1,1,1)
      else:
        return check(grid,row+dirrow,col+dircol,word,index+1,dirrow,dircol)
​
def word_search(letters, words):
  grid = list(map(lambda x: list(letters[x:x+8]), range(0,64,8)))
  found = []
  for row in range(8):
    for col in range(8):
      for word in words:
        if word not in found:
          if check(grid,row,col,word.upper()):
            found.append(word)
  return len(found) == len(words)

