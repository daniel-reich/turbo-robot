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
  horizontal, vertical = [letters[x:x+8] for x in range(0,64,8)], ["".join([letters[x] for x in range(y,64,8)]) for y in range(8)]
  diagonal = []
  for i in range(8):
    temp, temp2, temp3, temp4 = "", "", "", ""
    for j in range(8):
      if i +j <= 7:
        temp += horizontal[j][j+i]
      if j - i >= 0:
        temp2 += horizontal[j][j-i]
      if 7-(i +j) >= 0:
        temp3 += horizontal[j][abs(7-(j+i))]
      if 7-(j - i) <= 7:
        temp4 += horizontal[j][abs(7-(j-i))]
    if temp3 not in diagonal: diagonal.append(temp3)
    if temp4 not in diagonal: diagonal.append(temp4)
    if temp2 not in diagonal: diagonal.append(temp2)
    if temp not in diagonal: diagonal.append(temp)
  while len(words) > 0:
    start = len(words)
    for i in horizontal+vertical+diagonal:
      if words[-1].upper() in i or words[-1].upper() in i[::-1]:
        words.pop()
        break
    if len(words) == start: return False
  return True

