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
  upper_position = [c for c, i in enumerate(txt) if str(i).isalpha() and str(i).strip() and i.upper() == i]
  space_position = [c for c, i in enumerate(txt) if i == " "]
  txt = list(txt[::-1].lower().replace(" ", ""))
  for s in space_position:
      txt.insert(s, " ")
  for u in upper_position:
      txt[u] = txt[u].upper()
  return "".join(txt)

