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
  text = txt.split()
  ans = []
  for i in range(len(sorted(text, key=len)[-1])):
    lst = []
    for j in range(len(text)):
      if i >= len(text[j]):
        lst.append(" ")
      else:
        lst.append(text[j][i])
    ans.append(lst)
  return ans

