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
  txt = txt[::-1]
  new_txt = ''
  for char in txt:
    char = char.upper()
    new_txt += char
  return new_txt

