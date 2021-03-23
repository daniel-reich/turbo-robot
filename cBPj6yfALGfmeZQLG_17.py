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
    lst=txt.split(' ')
    max=0
    lst2=[]
    for i in lst:
        if len(i)>max:
            max=len(i)
    for i in lst:
        lst2.append(i+' '*(max-len(i)))
    result=[]
    for i in range(max):
        temp=[]
        for j in lst2:
            temp.append(j[i])
        result.append(temp)
    return result

