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
  Repeater = 1
  Chapter = ""
  for Char in txt.lower():
    if Repeater == 1:
      Chapter+=Char.upper()+"-"
    else:
      Chapter+=Char.upper()
      Chapter+=Char*(Repeater-1)+"-"
    Repeater+=1
  NewChapter = list(Chapter)
  NewChapter.pop()
  return "".join(NewChapter)

