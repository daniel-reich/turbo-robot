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
  if len(set(chars)) == len(chars):
    return '-1'
  return sorted(([i, x] for i, x in enumerate(chars) if x in chars[i+1:]), key=lambda x: x[0])[0][1]

