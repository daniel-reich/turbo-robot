"""


Creates a function that takes a string and returns the concatenated first and
last character.

### Examples

    first_last("ganesh") ➞ "gh"
    
    first_last("kali") ➞ "ki"
    
    first_last("shiva") ➞ "sa"
    
    first_last("vishnu") ➞ "vu"
    
    first_last("durga") ➞ "da"

### Notes

There is no empty string.

"""

def first_last(name):
  for i in range(len(name)):
    if i == 0:
      a = name[i]
    elif i == len(name) - 1:
      b = name [i]
  return a + b

