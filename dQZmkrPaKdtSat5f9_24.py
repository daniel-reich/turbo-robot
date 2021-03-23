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
  if txt == "":
    return ""
  txt1 = txt.lower()
  for i in set(txt1):
    if txt1.count(i) ==1:     
      return i.upper()

