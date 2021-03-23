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
    rows = [letters[n * 8:(n + 1) * 8] for n in range(8)]
    columns = ["".join((letters[n * 8 + i] for n in range(8))) for i in range(8)]
    l_diagonals = list("".join(letters[(range(0, 64, 9)[n] - a)] for n in range(a, 8)) for a in range(8)) + \
                  list("".join(letters[(range(0, 64, 9)[n] + a)] for n in range(0, 8 - a)) for a in range(1, 8))
    r_diagonals = list("".join(letters[(range(7, 64, 7)[n] + a)] for n in range(0, 8 - a)) for a in range(8)) + list(
        "".join(letters[(range(7, 64, 7)[n] + a)] for n in range(a, 8)) for a in range(1, 8))
    lines = rows + columns + l_diagonals + r_diagonals
    return all(any(word.upper() in line or word.upper() in line[::-1] for line in lines) for word in words)

