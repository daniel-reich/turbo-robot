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
  lst = [''] * 8
  for i in range(len(lst)):
    lst[i] = [''] * 8
  it = 0
  letters = letters.lower()
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      lst[i][x] = letters[it]
      it += 1
  rows, cols, rdiag, ldiag = [], [], [], []
  for i in range(len(lst[0])):
    cols.append(''.join([a[i] for a in lst]))
  rows = [''.join(i) for i in lst]
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      rtemp = ''
      ltemp = ''
      for a in range(8):
        if i+a < 8 and x+a < 8:
          rtemp += lst[i+a][x+a]
        if i+a < 8 and x-a >= 0:
          ltemp += lst[i+a][x-a]
      rdiag.append(rtemp)
      ldiag.append(ltemp)
  for i in words:
    if not any([i in a or i[::-1] in a for a in cols]):
      if not any([i in a or i[::-1] in a for a in rows]):
        if not any([i in a or i[::-1] in a for a in rdiag]):
          if not any([i in a or i[::-1] in a for a in ldiag]):
            return False
  return True

