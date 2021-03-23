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
  list = [letter for letter in txt]
  for i in range(len(list)):
    if ord(list[i])%2==0:
      list[i] = list[i].upper()
    else:
      list[i] = list[i].lower()
  return "".join(list)

