"""


Write a function that validates whether two strings are identical. Make it
case insensitive.

### Examples

    match("hello", "hELLo") ➞ True
    
    match("motive", "emotive") ➞ False
    
    match("venom", "VENOM") ➞ True
    
    match("mask", "mAskinG") ➞ False

### Notes

N/A

"""

def match(s1, s2):
  a = s1.lower()
  b = s2.lower()
  if a == b:
    return True
  else:
    return False

