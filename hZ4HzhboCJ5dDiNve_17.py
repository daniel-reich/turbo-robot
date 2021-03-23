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
  txt1 = txt.replace(' ', '')[::-1]
  txt2 = list(txt)
  for i in range(len(txt2)):
    if txt[i] != ' ':
      if txt[i].isupper():
        txt2[i] = txt1[0].upper()
      else:
        txt2[i] = txt1[0].lower()
      txt1 = txt1[1:]
  return ''.join(txt2)

