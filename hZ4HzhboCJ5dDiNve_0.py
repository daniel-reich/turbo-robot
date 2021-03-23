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
  l = [i.lower() for i in txt[::-1] if not i.isspace()]
  for i, c in enumerate(list(txt)):
    if c.isupper():
      l[i] = l[i].upper()
    elif c.isspace():
      l.insert(i, ' ')
  return ''.join(l)

