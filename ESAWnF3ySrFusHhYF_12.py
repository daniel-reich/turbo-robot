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
  def edit(word):
    word = list(reversed([l8r.upper() for l8r in word]))
    if len(word) % 2 == 0:
      return '-'.join([''.join(word[:len(word)//2]), ''.join(word[len(word)//2:])])
    else:
      return '-'.join([''.join(word[:(len(word)//2)+1]), ''.join(word[(len(word)//2)+1:])])
  
  return [edit(word) for word in lst]

