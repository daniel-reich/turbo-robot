"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
  import re
​
  spaces = [m.start() for m in re.finditer(' ', txt)]
  uppers = [i for i, c in enumerate(txt) if c.isupper()]
​
  result = re.sub(' ', '', txt)[::-1].lower()
  for index in spaces:
      result = result[:index] + ' ' + result[index:]
  return "".join(c.upper() if i in uppers else c for i, c in enumerate(result))

