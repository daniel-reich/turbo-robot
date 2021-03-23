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

############################################################
#   Sub Function
############################################################
​
def FNC_Word_Tweaker(Sample):
​
  if (Sample == ""):
    return "-"
  
  Length = len(Sample)
  
  if (Length % 2 == 0):
    Middle = int(Length / 2)
  else:
    Middle = int((Length + 1)/2)
    
  Sample = Sample.upper()
  Sample = Sample[::-1]
  
  Front = Sample[0:Middle]
  Back = Sample[Middle:]
  
  Output = Front + "-" + Back
  return Output
​
############################################################
#   MAIN FUNCTION
############################################################
​
def edit_words(lst):
  
  Answer = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    Word = lst[Counter]
    New = FNC_Word_Tweaker(Word)
    Answer.append(New)
    Counter += 1
  
  return Answer

