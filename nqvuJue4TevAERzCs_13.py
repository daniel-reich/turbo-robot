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
  count=0
  temp=list(txt)
  for i in temp:
    if (i.isdigit()):
      count+=1
    else:
      pass
  return count>0

