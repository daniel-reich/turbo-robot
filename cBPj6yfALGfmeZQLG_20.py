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
    l = len(max(txt.split(" "), key=len))
    result = [[] for i in range(0,l)]
    txt = txt.split(" ")
    for i in range(0,len(txt)):
        txt[i] += " "*(l-len(txt[i]))
    counter = 0
    for i in range(0,len(result)):
        result[i] = [y[counter] for y in txt]
        counter += 1
    return result

