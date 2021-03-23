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
    sht, lng = min(len(w) for w in words), max(len(w) for w in words)
    words = [w.upper() for w in words]
    for i in range(len(letters)):
        wrdset = set(w for w in words if w.startswith(letters[i]))
        if wrdset:
            for dr, dc in [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]:
                wrd = letters[i]
                r, c = (i // 8)+dr, (i % 8)+dc
                wset = wrdset.copy()
                while 0<=r<8 and 0<=c<8 and len(wrd)<lng and len(wset)>0:
                    wrd += letters[r*8+c]
                    wset = {w for w in wset if w.startswith(wrd)}
                    if len(wrd) >= sht:
                        if wrd in wset:
                            words.remove(wrd)
                            wset.remove(wrd)
                            wrdset.remove(wrd)
                            break
                    r += dr
                    c += dc
                if len(words) == 0:
                    return True
                if not wrdset:
                    break
    return False

