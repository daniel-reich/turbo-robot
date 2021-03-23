"""


Create a function that converts a string into a matrix of characters that can
be read vertically. Add spaces when characters are missing.

### Examples

    vertical_txt("Holy bananas") ➞ [
      ["H", "b"],
      ["o", "a"],
      ["l", "n"],
      ["y", "a"],
      [" ", "n"],
      [" ", "a"],
      [" ", "s"]
    ]
    
    vertical_txt("Hello fellas") ➞ [
      ["H", "f"],
      ["e", "e"],
      ["l", "l"],
      ["l", "l"],
      ["o", "a"],
      [" ", "s"]
    ]

### Notes

N/A

"""

def vertical_txt(txt):
  txtlst = txt.split()
  m = max(len(w) for w in txtlst)
  res = []
  for i,w in enumerate(txtlst):
    tmp = []
    for j in range(m):
      tmp.append(w[j] if j < len(w) else ' ')
    res.append(tmp)
  return list(map(list,zip(*res)))

