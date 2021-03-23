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
  vert1 = txt.split(' ')
  lenLst = [len(i) for i in vert1]
  longestWord = lenLst.index(max(lenLst))
  vert2 = [[' ' for i in vert1] for i in vert1[longestWord]]
  for worCounter, word in enumerate(vert1):
    for letCounter, letter in enumerate(word):
      vert2[letCounter][worCounter] = letter
  return vert2

