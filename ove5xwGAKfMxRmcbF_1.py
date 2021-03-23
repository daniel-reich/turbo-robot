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
  return s1.upper()==s2.upper()

