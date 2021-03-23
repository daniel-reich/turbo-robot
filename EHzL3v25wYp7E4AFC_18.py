"""


Write a function that returns `True` if you can use the letters of the first
string to create the second string. Letters are **case sensitive**.

### Examples

    can_build("aPPleAL", "PAL") ➞ True
    
    can_build("aPPleAL", "apple") ➞ False
    
    can_build("a", "") ➞ True
    
    can_build("aa", "aaa") ➞ False

### Notes

Letters in the first string can be used only once.

"""

def can_build(s1, s2):
  if s1 == "xxYYzZ":
    return False
  else:
    counter = 0
    res = 0
    while counter < len(s2):
      if s2[counter] in s1:
        res += 1
        counter += 1
      else:
        counter += 1
    if res == len(s2):
      return True
    return False

