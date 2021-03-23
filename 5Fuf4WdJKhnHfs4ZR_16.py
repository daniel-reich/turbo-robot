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
  return sum([1 for i in s])

