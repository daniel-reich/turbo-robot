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
  v = [i for i in txt if i != ' '][::-1]
  s, j = '', 0
  for i in txt:
    if i == ' ':
      s = s + ' '
    else:
      if i.isupper():
        s = s + v[j].upper()
      elif i.islower():
        s = s + v[j].lower()
      else:
        s = s + v[j].lower()
      j = j + 1
  return s

