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
  first = name[0]
  last = name[-1]
  first_and_last = first + last
  return first_and_last

