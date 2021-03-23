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
    lst = txt.split()
    mx = len(max(lst, key = lambda x: len(x)))
    print(lst, mx)
​
    tbl = [[' ' for i in range(len(lst))] for j in range(mx)]
    print(tbl)
​
    col = 0
    for wd in lst:
        for row in range(len(wd)):
            tbl[row][col] = wd[row]
        col += 1
​
    return tbl

