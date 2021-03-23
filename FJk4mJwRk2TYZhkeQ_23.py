"""


Create a function that takes a string and returns a new string with each new
character accumulating by +1. Separate each set with a dash.

### Examples

    accum("abcd") ➞ "A-Bb-Ccc-Dddd"
    
    accum("RqaEzty") ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    
    accum("cwAt") ➞ "C-Ww-Aaa-Tttt"

### Notes

  * Capitalize the first letter of each set.
  * All tests contain valid strings with alphabetic characters (a-z, A-Z).

"""

def accum(txt):
  newlst = []
  n = 1
  for char in txt:
    newlst.append(char * n)
    n += 1
  for entry in newlst:
    newlst[newlst.index(entry)] = entry.title()
  return '-'.join(newlst)

