"""


Create a function that takes a string of lowercase characters and returns that
string reversed and in upper case.

### Examples

    reverse_capitalize("abc") ➞ "CBA"
    
    reverse_capitalize("hellothere") ➞ "EREHTOLLEH"
    
    reverse_capitalize("input") ➞ "TUPNI"

### Notes

N/A

"""

def reverse_capitalize(txt):
  a=txt[::-1]
  b=a.upper()
  return b
