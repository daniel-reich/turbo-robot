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
  num = 0
  txt = txt.upper()
  if txt == '': return ''
  for one in txt:
    for test in txt:
      if one == test : num +=1
      
    if num == 1:
      return one
    num = 0

