"""


Write a function that splits a string into substrings of size n, adding a
specified delimiter between each of the pieces.

### Examples

    split_and_delimit("bellow", 2, "&") ➞ "be&ll&ow"
    
    split_and_delimit("magnify", 3, ":") ➞ "mag:nif:y"
    
    split_and_delimit("poisonous", 2, "~") ➞ "po~is~on~ou~s"

### Notes

N/A

"""

def split_and_delimit(txt, num, delimiter):
  
  Passage = ""
  
  Counter = 0
  Length = len(txt)
  
  
  while (Counter < Length):
    
    Item = txt[Counter]
    
    if (Counter % num == 0) and (Counter != 0):
      Passage = Passage + delimiter
      Passage = Passage + Item
      Counter += 1
    else:
      Passage = Passage + Item
      Counter += 1
  
  return Passage

