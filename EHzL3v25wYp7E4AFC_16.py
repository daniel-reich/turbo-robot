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

from collections import Counter
def can_build(s1, s2):
  return all(v <= Counter(s1)[k] for k,v in Counter(s2).items())

