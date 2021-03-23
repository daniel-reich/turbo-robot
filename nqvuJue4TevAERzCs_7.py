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
  l=[str(c) for c in range(10)]
  if any([t in l for t in txt]):
    return True
  else:
    return False

