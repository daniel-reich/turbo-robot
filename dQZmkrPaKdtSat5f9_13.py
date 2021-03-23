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

from collections import Counter
def single_occurrence(txt):
  if txt:
    d=Counter(txt.upper())
    k={x:y for y,x in d.items()}
    return k[min(d.values())]
  else:return ''

