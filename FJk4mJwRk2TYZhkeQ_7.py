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
  count = 1
  words = []
  for c in txt:
    s = c.lower() * (count-1)
    s = c.upper() + s
    words.append(s)
    count += 1
  return '-'.join(words)

