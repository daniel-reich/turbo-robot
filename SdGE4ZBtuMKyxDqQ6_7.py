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
  count=0
  for i in range(0,len(chars)):
    if chars[i+1:].count(chars[i]) > 0:
        return chars[i]
        break
    else:
      count+=1
  if count == len(chars):
    return "-1"

