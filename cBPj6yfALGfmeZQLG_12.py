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
  try:
    lst = txt.split(" ")
    size = max([len(word) for word in lst])
    array = [[" " for i in range(len(lst))] for j in range(size)]
​
    col = 0
    for word in lst:
      row = 0
      for letter in word:
        array[row][col] = letter
        row += 1
      col += 1
​
    return array
  except IndexError:
    return size

