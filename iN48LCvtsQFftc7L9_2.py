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

def make_table(txt, length=8):
    res, txt = [], txt.lower()
    while txt:
        res.append(txt[:length])
        txt = txt[length:]
    return res
​
​
def make_words_list(table, position=(0, 0)):
    m, n, row, col = len(table), len(table[0]), position[0], position[1]
    res = list()
    res.append(''.join(table[row][j] for j in range(col, n)))
    res.append(''.join(table[i][col] for i in range(row, m)))
    res.append(''.join(table[row][j] for j in range(col, -1, -1)))
    res.append(''.join(table[i][col] for i in range(row, -1, -1)))
    res.append(''.join(table[row + k][col + k]
                       for k in range(min(m - row, n - col))))
    res.append(''.join(table[row - k][col - k]
                       for k in range(min(row, col) + 1)))
    res.append(''.join(table[row - k][col + k]
                       for k in range(min(row + 1, n - col))))
    res.append(''.join(table[row + k][col - k]
                       for k in range(min(m - row, col + 1))))
    return res
​
​
def find_letter(table, c):
    return [[i, j] for i, row in enumerate(table) for j, ch in enumerate(row)
            if ch == c]
​
​
def word_search(letters, words):
    table = make_table(letters, 8)
    for word in words:
        word_found = False
        for position in find_letter(table, word[0]):
            for made_word in make_words_list(table, position):
                if made_word.startswith(word):
                    word_found = True
                    break
            if word_found:
                break
        if not word_found:
            return False
    return True

