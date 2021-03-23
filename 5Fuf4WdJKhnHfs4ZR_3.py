"""


Create a function which returns the length of a string, without using `len()`.

### Examples

    length("Hello World") ➞ 11
    
    length("Edabit") ➞ 6
    
    length("wash your hands!") ➞ 16

### Notes

N/A

"""

def length(s):
  pos = 0
  for p in s:
    pos += 1
  return pos

