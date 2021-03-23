"""


Create a function that takes a string and returns the first character that
repeats. If there is no repeat of a character, then return "-1".

### Examples

    first_repeat("legolas") ➞ "l"
    
    first_repeat("Gandalf") ➞ "a"
    
    first_repeat("Balrog") ➞ "-1"
    
    first_repeat("Isildur") ➞ "-1"

### Notes

Tests are case sensitive.

"""

def first_repeat(chars):
  y = ''
  b = ''
  for x in chars:
    if x in y:
      b +=x
    else:
      y += x
  if b == '':
    return '-1'
  return b[0]

