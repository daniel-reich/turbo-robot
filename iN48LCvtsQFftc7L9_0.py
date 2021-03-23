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

def word_search(letters, words,):
    rows = [letters[idx*8:idx*8+8] for idx in range(8)]
    columns = [letters[idx::8] for idx in range(8)]
    rdiags = [letters[idx:64-idx*8:9] for idx in range(8)] +\
            [letters[8*idx::9] for idx in range(1,8)]
    ldiags = [letters[idx:idx*8+1:7] for idx in range(8)] +\
            [letters[15+8*idx::7] for idx in range(7)]
    def contains(word):
        return any(token in string for string in rows+columns+rdiags+ldiags
                  for token in [word, word[::-1]])
    return all(contains(word.upper()) for word in words)

