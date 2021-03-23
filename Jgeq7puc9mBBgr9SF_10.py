"""


Create a function which adds _zeros_ to the **start** of a binary string, so
that its length is a **mutiple of 8**.

### Examples

    complete_binary("1100") ➞ "00001100"
    
    complete_binary("1101100") ➞ "01101100"
    
    complete_binary("110010100010") ➞ "0000110010100010"

### Notes

Return the same string if its length is already a multiple of 8.

"""

def complete_binary(s):
  return s[:len(s)%8].zfill(8) + s[len(s)%8:] if len(s)%8 else s

