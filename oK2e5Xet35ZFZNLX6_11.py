"""


Create a function that takes a string and checks if every single character is
**preceded and followed** by a character adjacent to it in the _english
alphabet_.

Example: "b" should be preceded and followed by ether "a" or "c" (`abc || cba
|| aba || cbc == True` but `abf || zbc == False`).

### Examples

    neighboring("aba") ➞ True
    
    neighboring("abcdedcba") ➞ True
    
    neighboring("efghihfe") ➞ False
    
    neighboring("abc") ➞ True
    
    neighboring("qrstuv") ➞ True
    
    neighboring("mnopqrtstrqpomn") ➞ True

### Notes

All test cases will consist of lower case letters only.

"""

def neighboring(txt, i=0):
  if i == len(txt) - 1:
    return True
  a = 'abcdefghijklmnopqrstuvwxyz'
  try:
    if txt[i+1] == a[a.index(txt[i]) + 1] or txt[i+1] == a[a.index(txt[i]) - 1]:
      return neighboring(txt, i+1)
    else:
      return False
  except IndexError:
    return True

