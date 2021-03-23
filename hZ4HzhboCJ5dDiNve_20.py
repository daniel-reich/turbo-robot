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

import re
def special_reverse_string(txt):
  form = re.sub(r'[^\s]', '{}', txt)
  cases = [i.isupper() for i in txt if i != " "]
  chars = [i for i in txt if i != " "]
  print(txt, form, cases, chars)
  chars = [b.upper() if a else b.lower() for a, b in zip(cases, chars[::-1])]
  return form.format(*chars)

