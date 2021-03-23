"""


Create a function that takes a string as input and capitalizes a letter if its
ASCII code is even and returns its lower case version if its ASCII code is
odd.

### Examples

    ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
    
    ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
    
    ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."

### Notes

N/A

"""

def ascii_capitalize(txt):
  a =""
  for i in txt:
    if ord(i) % 2 == 0:
      b = i.upper()
      a+=b
    elif ord(i) % 2 != 0:
      c = i.lower()
      a+=c
  return a

