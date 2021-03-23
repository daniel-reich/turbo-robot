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
    safe = []
    grid = [list(letters[x:x+8]) for x in range(0, 64, 8)]
    for x in words:
        x = x.upper()
        if x in letters or x[::-1] in letters:
            safe.append(True)
            continue
        for row in range(8):
            for col in range(8):
                if grid[row][col] == x[0]:
                    d = row + len(x) - 1 < 8
                    u =  row - len(x) >= -1
                    if d:
                        c = ''.join([grid[row+d][col] for d in range(len(x))])
                        if c == x or c[::-1] == x:
                            safe.append(True)
                    if u:
                        c = ''.join([grid[row-d][col] for d in range(len(x))])
                        if c == x or c[::-1] == x:
                            safe.append(True)
                            
​
                    if row + len(x) < 8 and col - len(x) >= -1:
                        c = ''.join(grid[row+d][col-d] for d in range(len(x)))
                        if c == x or c[::-1] == x:
                            safe.append(True)
                    
                    if row + len(x) < 8 and col + len(x) <= 8:
                        c = ''.join(grid[row+d][col+d] for d in range(len(x)))
                        if c == x or c[::-1] == x:
                            safe.append(True)
​
                    if u and col + len(x) <= 8:
                        c = ''.join(grid[row-d][col+d] for d in range(len(x)))
                        if c == x or c[::-1] == x or c in words or c[::-1] in words:
                            safe.append(True)
                    
                    if u and col - len(x) >= -1:
                        c = ''.join(grid[row-d][col-d] for d in range(len(x)))
                        if c == x or c[::-1] == x or c[::-1] in words:
                            safe.append(True)
​
    return len(safe) == len(words)

