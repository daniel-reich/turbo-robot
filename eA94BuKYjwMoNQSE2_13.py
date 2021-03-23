"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

def correct_signs(txt):
  chars = txt.split(" ")
  for i in range(2, len(chars), 2):
    if chars[i-1] == ">":
      if not(int(chars[i-2]) > int(chars[i])):
        return False
    elif not(int(chars[i-2]) < int(chars[i])):
      return False
  return True

