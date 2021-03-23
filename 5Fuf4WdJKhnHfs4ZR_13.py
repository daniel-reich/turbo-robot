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
  n=0
  for i in s:
    n+=1
  return n

