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
  lst = []
  for i in range(len(txt)):
    lst.append(txt[i].capitalize() + txt[i].lower() * i)
  new_txt = "-".join(lst)
  return new_txt

