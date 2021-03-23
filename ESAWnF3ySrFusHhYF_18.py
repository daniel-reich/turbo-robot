"""


Create a function that takes a list of any _length_. Modify each element
**(capitalize, reverse, hyphenate)**.

### Examples

    edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]
    
    edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]
    
    edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]
    
    edit_words([""]) ➞ ["-"]

### Notes

Input list values can be any _type_.

"""

def edit_words(lst):
  return [hyphenate(x).upper()[::-1] for x in lst]
    
    
    
def hyphenate(word):
  if len(word) == 0:
    return '-'
  middle = len(word) // 2
  word = list(word)
  newlist = []
  for i in range(len(word)):
    if i == middle:
      newlist.append('-')
      newlist.append(word[i])
    else:
      newlist.append(word[i])
  return ''.join(newlist)

