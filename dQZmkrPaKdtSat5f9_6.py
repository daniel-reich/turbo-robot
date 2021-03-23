"""


Create a function that, given a string `txt`, finds a letter that has a single
occurrence. Return the letter in uppercase. If the input is empty, return an
empty string `""`.

### Examples

    single_occurrence("EFFEAABbc") ➞ "C"
    
    single_occurrence("AAAAVNNNNSS") ➞ "V"
    
    single_occurrence("S") ➞ "S"

### Notes

The function will not be case sensitive.

"""

def single_occurrence(txt):
  
  txt = txt.upper()
  Answer = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Item = txt[Counter]
    Events = txt.count(Item)
    
    if (Events == 1):
      Answer = Item
      return Answer
    else:
      Counter += 1
      
  return Answer

