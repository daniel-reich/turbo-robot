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
  new_lst=[]
  for word in lst:
    if len(word)>0:
      if len(word)%2==0:
        hyp_pos = len(word)/2
      else:
        hyp_pos = int(len(word)/2)+1
      count = 0
      new_word = ""
    else:
      new_word = "-"
    for letter in list(reversed(word)):
      letter = letter.upper()
      if count+1 == hyp_pos:
        hyphenation = letter+"-"
        new_word+=hyphenation
        count+=1
      else:
        new_word+=letter
        count+=1
    new_lst.append(new_word)
    
  return new_lst

