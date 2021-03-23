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

import re
def has_digit(txt):
  tester = re.findall("[0-9]", txt)
  tester = ''.join(tester)
  if tester.isalnum():
    return True
  else:
    return False

