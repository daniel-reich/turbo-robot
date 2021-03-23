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
    out = []
    word_list = []
    for  i in range(0,len(letters),8):
        word_list.append(list(letters[i:i+8]))
    for m in range(len(word_list)):
        h = ''; v = '';
        for n in range(len(word_list)):
            d1 = ''; d2 = ''; d3 = ''; d4 = ''
            h += word_list[m][n]
            v += word_list[n][m]
            a = m
            b = n
            c = m
            d = n
            while a < len(word_list) and b<len(word_list):
                d1 += word_list[a][b]
                a += 1
                b += 1
            out.append(d1)
            while c < len(word_list) and d>=0:
                d2 += word_list[c][d]
                c += 1
                d -= 1
            out.append(d2)
            e = m; f = n
            while e >=0 and f>= 0:
                d3 += word_list[e][f]
                print(d3)
                e -= 1
                f -=1
            out.append(d3)
            g = m;o = n
            while g>= 0 and o<len(word_list):
                d4 += word_list[g][o]
                g -= 1
                o += 1
            out.append(d4)
        out.append(h)
        out.append(v)
    t = []
    for w in words:
        for word in out:
            if w in word.lower() or w[::-1] in word.lower():
                t.append(w)
    if len(set(t)) == len(words):
        return True
    return False

