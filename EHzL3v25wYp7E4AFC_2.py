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

def can_build(a,b):
  l=len(a)
  for x in b:
    a=a.replace(x,'',1)
  return l==len(a)+len(b)

