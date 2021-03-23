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

def find_word(table, ttable, word):
    word = word.lower()
    L = len(word)
    for row in table:
        if word in row or word in row[::-1]:
            return True
    for row in ttable:
        if word in row or word in row[::-1]:
            return True
    # find diagonal words:
    for row in range(8):
        for col in range(8):
            for dr, dc in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                r, c = row, col
                diag = ""
                while 0 <= r < 8 and 0 <= c < 8 and len(diag) < L:
                    diag += table[r][c]
                    if diag == word:
                        return True
                    r += dr
                    c += dc
    return False
    
def word_search(letters, words):
    table = []
    for k in range(8):
        table.append(letters.lower()[8*k:8*k+8])
    ttable = [''.join(list(i)) for i in zip(*table)]
    return all([find_word(table, ttable, word) for word in words])

