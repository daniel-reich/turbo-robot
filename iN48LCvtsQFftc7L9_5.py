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

def can_be_found(word,group):
  for g in group:
    if word.upper() in g:
      return True
    elif word[::-1].upper() in g:
      return True
  return False
​
def word_search(letters, words):
  lst = list(map(lambda x: ''.join(letters[x:8+x]),range(0,64,8)))
  lst.extend(list(map(lambda x: ''.join(letters[x:64:8]),range(0,8))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[x+(9*y)],range(0,8-x)))),range(0,6))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[8*x + 9*y],range(0,8-x)))),range(1,6))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[x+(7*y)],range(0,x+1)))),range(2,8))))
  lst.extend(list(map(lambda x: ''.join(list(map(lambda y: letters[(8*x - 1) + 7*y],range(0,9-x)))),range(2,7))))
  
  for word in words:
    if can_be_found(word,lst) == False:
      return False
  return True

