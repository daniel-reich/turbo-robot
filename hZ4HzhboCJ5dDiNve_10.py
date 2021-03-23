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
  stripped = ''
  for i in txt:
    if i != ' ':
      stripped += i
    reversed = stripped[::-1]
  output = ''
  for i in range(len(txt)):
    if txt[i] == ' ':
      output += ' '
    elif txt[i].islower():
      output += reversed[0].lower()
      try:
        reversed = reversed[1:]
      except:
        pass
    elif txt[i].isupper():
      output += reversed[0].upper()
      try:
        reversed = reversed[1:]
      except:
        pass
    else:
      output += reversed[0].lower()
      try:
        reversed = reversed[1:]
      except:
        pass
  return output

