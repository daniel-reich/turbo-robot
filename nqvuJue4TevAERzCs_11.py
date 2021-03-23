"""


Write a regular expression that matches a string if it contains at least one
digit.

### Examples

    has_digit("c8") ➞ True
    
    has_digit("23cc4") ➞ True
    
    has_digit("abwekz") ➞ False
    
    has_digit("sdfkxi") ➞ False

### Notes

This challenge is designed to use RegEx only.

"""

def has_digit(txt):
  txtList = []
  for character in txt:
    txtList.append(character)
​
  for character in txtList:
    try:
      convert = int(character)
      return True
    except:
      continue
​
  return False

