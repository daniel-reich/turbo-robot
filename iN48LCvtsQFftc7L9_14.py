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

def word_search(letters, words):
  horiz = [letters[8*i:(8*i)+8].lower() for i in range(8)]
  vert = [''.join(letters[8*i + j].lower() for i in range(8)) for j in range(8)] 
​
  diagr = []
  diagl = []
  for i in range(15):
    diagr.append('')
    diagl.append('')
    
  for i in range(8):
    for j in range(8):
      diagr[i+j] += horiz[i][j]
      diagl[i+j] += horiz[i][7-j]
​
  for word in words:
    found = False
    wordr = word[::-1]
    found = found or any(word in horiz[i] for i in range(len(horiz)))
    found = found or any(word in vert[i] for i in range(len(vert)))
    found = found or any(word in diagr[i] for i in range(len(diagr)))
    found = found or any(word in diagl[i] for i in range(len(diagl)))
    found = found or any(wordr in horiz[i] for i in range(len(horiz)))
    found = found or any(wordr in vert[i] for i in range(len(vert)))
    found = found or any(wordr in diagr[i] for i in range(len(diagr)))
    found = found or any(wordr in diagl[i] for i in range(len(diagl)))
    if not found:
      return False
  return True

