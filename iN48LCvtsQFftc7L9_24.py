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

def word_search(x,l):
    g=[]
    q=[]
    t=0
    for i in range(1,len(x)+1):
        if i%8==0:
            g.append(q+[x[i-1]])
            q=[]
        else:
            q.append(x[i-1])
    for w in l:
        w=w.upper()
        p=w[::-1]
        for r in range(len(g)):
            if w in ''.join(g[r])or p in ''.join(g[r]):
                t+=1
        for c in range(len(g[0])):
            cw = ''
            for r in range(len(g)):
                cw += g[r][c]
            if w in cw or p in cw:
                t+=1    
        f=''
        for a in range(15,-1,-1):
            for r in range(8):
                a-=1
                for c in range(8):
                    if a==c:
                        f+=g[r][c]
            if w in f or p in f:
                t+=1
            f=''
        for a in range(-8,8,1):
            for r in range(8):
                a+=1
                for c in range(8):
                    if a==c:
                        f+=g[r][c]
            if w in f or p in f:
                t+=1
            f=''
    return t>=len(l)

