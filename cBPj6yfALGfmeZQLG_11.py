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
    t=txt.split()
    m=len(max(t,key=len))
    a=[[' 'for x in range(len(t))] for y in range(m)]
    for x in range(m):
        for y in range(len(t)):
            if x<len(t[y]):
                a[x][y]=t[y][x]
    return a

